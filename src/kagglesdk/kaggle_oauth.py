import base64
import hashlib
import http.server
import logging
import os
import platform
import random
import secrets
import socketserver
import uuid
import urllib.parse
import webbrowser
from datetime import datetime, timedelta, timezone
from kagglesdk.kaggle_client import KaggleClient
from kagglesdk.kaggle_creds import KaggleCredentials
from kagglesdk.security.types.oauth_service import ExchangeOAuthTokenRequest


class KaggleOAuth:
    OAUTH_CLIENT_ID = "kagglesdk"

    def __init__(self, client: KaggleClient):
        self._client = client
        self._http_client = client.http_client()
        self._server_running = False
        self._creds = None
        self._logger = logging.getLogger(__name__)

    class OAuthState:
        def __init__(self):
            self.state = str(uuid.uuid4())
            self.code_verifier = KaggleOAuth.OAuthState._generate_code_verifier()
            self.code_challenge = KaggleOAuth.OAuthState._generate_code_challenge(self.code_verifier)

        def _generate_state(length: int = 32):
            return secrets.token_urlsafe(length)

        def _generate_code_verifier(length: int = 64) -> str:
            if not 42 <= length <= 128:
                raise ValueError("Code verifier length must be between 42 and 128 characters.")
            return secrets.token_urlsafe(length)

        def _generate_code_challenge(code_verifier: str) -> str:
            code_verifier_bytes = code_verifier.encode("utf-8")
            code_challenge_bytes = hashlib.sha256(code_verifier_bytes).digest()
            code_challenge_base64 = base64.urlsafe_b64encode(code_challenge_bytes).decode("utf-8")
            return code_challenge_base64

    class OAuthCallbackHandler(http.server.BaseHTTPRequestHandler):
        def __init__(
            self,
            *args,
            oauth: "KaggleOAuth" = None,
            oauth_state: "KaggleOAuth.OAuthState" = None,
            on_success=None,
            logger=None,
            **kwargs,
        ):
            self._oauth = oauth
            self._oauth_state = oauth_state
            self._on_success = on_success
            self._logger = logger
            super().__init__(*args, **kwargs)

        def do_GET(self):
            if self.path == "/favicon.ico":
                return
            try:
                self._handle_oauth_callback()
            finally:
                self._stop_server()

        def _handle_oauth_callback(self):
            parsed_url = urllib.parse.urlparse(self.path)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            if "code" in query_params and "state" in query_params:
                code = query_params["code"][0]
                state = query_params["state"][0]
                self._logger.debug(f"\nReceived OAuth Callback:")
                self._logger.debug(f"  code : {code}")
                self._logger.debug(f"  state: {state}")
                if state == self._oauth_state.state:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(
                        b"<html><body><h1>Authentication Successful!</h1><p>You can close this window.</p></body></html>"
                    )
                    self._on_success(code)
                else:
                    self._logger.error(f"Invalid state! Expected: {self._oauth_state.state}, Received: {state}")
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(b"<html><body><h1>Authentication Failed!</h1></body></html>")
            else:
                self._logger.debug(f"\nReceived Invalid OAuth Callback: {self.path}")
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(
                    b"<html><body><h1>Authentication Failed!</h1><p>Invalid callback parameters.</p></body></html>"
                )

        def _stop_server(self):
            self._oauth.stop_server()

    @staticmethod
    def _can_open_browser():
        if platform.system() in ["Windows", "Darwin"]:
            return True  # Assume GUI on Windows/Mac

        if "DISPLAY" in os.environ and os.environ["DISPLAY"] != "":
            return True  # X11 display available

        return False

    def _exchange_oauth_token(self, code: str, scopes: list[str], oauth_state: "KaggleOAuth.OAuthState"):
        request = ExchangeOAuthTokenRequest()
        request.code = code
        request.code_verifier = oauth_state.code_verifier
        request.grant_type = "authorization_code"

        response = self._client.security.oauth_client.exchange_oauth_token(request)
        self._creds = KaggleCredentials(
            client=self._client,
            refresh_token=response.refreshToken,
            access_token=response.accessToken,
            access_token_expiration=datetime.now(timezone.utc) + timedelta(seconds=response.expires_in),
            username=response.username,
            scopes=scopes,
        )

    def _run_oauth_flow(self, scopes: list[str], no_launch_browser: bool) -> KaggleCredentials:
        use_browser = not no_launch_browser and KaggleOAuth._can_open_browser()
        redirect_uri = self._http_client.get_oauth_default_redirect_url()
        if use_browser:
            port = random.randint(8000, 9000)
            redirect_uri = f"http://localhost:{port}"
            self._logger.debug(f"Will listen for the callback at: {redirect_uri}")

        oauth_state = KaggleOAuth.OAuthState()
        oauth_start_url = self._http_client.build_start_oauth_url(
            client_id=KaggleOAuth.OAUTH_CLIENT_ID,
            redirect_uri=redirect_uri,
            scope=scopes,
            state=oauth_state.state,
            code_challenge=oauth_state.code_challenge,
        )

        if use_browser:
            webbrowser.open(oauth_start_url)
            print("Your browser has been opened to visit:")
            print(f"  {oauth_start_url}\n\n")

            def exchange_oauth_token(code: str):
                self._exchange_oauth_token(code, scopes, oauth_state)

            def handler_factory(*args, **kwargs):
                return KaggleOAuth.OAuthCallbackHandler(
                    *args,
                    oauth=self,
                    oauth_state=oauth_state,
                    on_success=exchange_oauth_token,
                    logger=self._logger,
                    **kwargs,
                )

            self._server_running = True
            with socketserver.TCPServer(("127.0.0.1", port), handler_factory) as httpd:
                self._logger.debug(f"Listening for callback on port {port}...")
                while self._server_running:
                    httpd.handle_request()
                self._logger.debug("OAuth flow completed (or server stopped).")
        else:
            print("\nGo to the following link in your browser, and complete the sign-in prompts at Kaggle:\n")
            print(f"  {oauth_start_url}")
            print(
                "\nOnce finished, enter the verification code provided in your browser: ",
                end="",
            )
            code = input()
            self._exchange_oauth_token(code, scopes, oauth_state)

        return self._creds

    def stop_server(self):
        self._server_running = False

    def _ensure_creds_valid(self, creds: KaggleCredentials):
        if not creds:
            raise Exception("Authentication failed.")
        return creds.introspect()

    def authenticate(self, scopes: list[str], no_launch_browser: bool = False) -> KaggleCredentials:
        creds = self._run_oauth_flow(scopes, no_launch_browser)
        username = self._ensure_creds_valid(creds)
        creds.save()
        print(f"\nYou are now logged in as [{username}]\n")
        return creds
