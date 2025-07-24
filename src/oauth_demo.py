import os
import uuid
import json
from flask import Flask, redirect, request, session, render_template_string
from kagglesdk.kaggle_client import KaggleClient
from kagglesdk.kaggle_env import KaggleEnv
from kagglesdk.security.types.oauth_service import ExchangeOAuthTokenRequest, IntrospectTokenRequest
from requests.exceptions import HTTPError

app = Flask(__name__)
# It's important to set a secret key for session management.
# In a real application, use a more secure, randomly generated key stored securely.
app.secret_key = os.urandom(24)

# --- Kaggle Client ---
# Instantiate the Kaggle client to interact with Kaggle APIs.
client = KaggleClient(
    env=KaggleEnv.LOCAL,
    verbose=True,
    username='kusanagi31415',
    api_token='KGAT_45a83036c74c0393fdf89eeb9833b4f7')

# --- Configuration ---
OAUTH_CLIENT_ID = "org:auto-kaggle"
# This must match the redirect URI registered with your OAuth provider
REDIRECT_URI = "http://localhost:8000/oauth/callback"

# --- HTML Templates ---

# Template for the main login page
LOGIN_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kaggle OAuth Demo</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f4f4f9; }
        .container { text-align: center; padding: 40px; background-color: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        .login-button { display: inline-block; padding: 12px 24px; background-color: #20beff; color: white; text-decoration: none; border-radius: 4px; font-size: 16px; transition: background-color 0.3s; }
        .login-button:hover { background-color: #0099e5; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Kaggle OAuth Demo</h1>
        <p>Click the button below to sign in with your Kaggle account.</p>
        <a href="/login" class="login-button">Login with Kaggle</a>
    </div>
</body>
</html>
"""

# Template for displaying the results after successful authentication
RESULT_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Authentication Successful</title>
    <style>
        body { font-family: sans-serif; background-color: #f4f4f9; padding: 20px; color: #333; }
        .container { max-w: 800px; margin: auto; background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { color: #4CAF50; }
        h2 { border-bottom: 2px solid #eee; padding-bottom: 10px; }
        pre { background-color: #f0f0f0; padding: 15px; border-radius: 4px; white-space: pre-wrap; word-wrap: break-word; }
        .token { color: #D83B01; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Authentication Successful!</h1>
        <p>You have successfully authenticated with Kaggle. Below are your tokens and introspection details.</p>
        
        <h2>Access Token</h2>
        <pre><span class="token">{{ access_token }}</span></pre>

        <h2>Refresh Token</h2>
        <pre><span class="token">{{ refresh_token }}</span></pre>

        <h2>Token Introspection Details</h2>
        <pre>{{ introspection_details }}</pre>
    </div>
</body>
</html>
"""

# --- Flask Routes ---

@app.route("/")
def index():
    """Renders the main login page."""
    return render_template_string(LOGIN_PAGE_TEMPLATE)

@app.route("/login")
def login():
    """Redirects the user to the Kaggle OAuth authorization URL."""
    # Generate a random state to prevent CSRF attacks
    state = str(uuid.uuid4())
    session['oauth_state'] = state

    # Use KaggleClient to build the authorization URL
    default_scopes = ["resources.admin:*"]
    auth_url = client.http_client().build_start_oauth_url(
        client_id=OAUTH_CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        scope=default_scopes,
        state=state,
        code_challenge=None,  # Set to None as PKCE is not required for this demo
    )
    
    # Redirect user to Kaggle's authorization page
    return redirect(auth_url)

@app.route("/oauth/callback")
def oauth_callback():
    """
    Handles the callback from Kaggle after user authorization.
    Exchanges the authorization code for an access token and refresh token.
    """
    # Extract authorization code and state from the query parameters
    code = request.args.get("code")
    state = request.args.get("state")

    # Verify the state to ensure the request is legitimate
    # if not state or state != session.get('oauth_state'):
    #     return "Invalid state. Authentication failed.", 400

    try:
        # Exchange the authorization code for tokens using KaggleClient
        exchange_req = ExchangeOAuthTokenRequest()
        exchange_req.grant_type = "authorization_code"
        exchange_req.code = code
        # The redirect_uri and client_id are typically handled by the client's configuration
        try:
            token_response = client.security.oauth_client.exchange_oauth_token(exchange_req)
        except HTTPError as e:
            return f"An HTTP error occurred: {e.response.status_code} {e.response.reason}<br><pre>{e.response.text}</pre>", 500
        except Exception as e:
            # It's helpful to see the actual response from the server on error
            error_details = f"Exception type: {type(e)}\n"
            error_details += f"Exception: {e}\n"
            error_details += f"Exception attributes: {dir(e)}"
            return f"An error occurred: <pre>{error_details}</pre>", 500

        access_token = token_response.accessToken
        refresh_token = token_response.refreshToken

        if not access_token:
            return "Failed to retrieve access token.", 500

        # Use the access token to get token introspection details using KaggleClient
        introspect_req = IntrospectTokenRequest()
        introspect_req.token = access_token
        introspect_resp = client.security.oauth_client.introspect_token(introspect_req)

        # Format introspection details for a readable display
        introspection_details = {
            "active": introspect_resp.active,
            "username": introspect_resp.username,
            "scope": introspect_resp.scope,
            "client_id": introspect_resp.client_id,
        }
        
        # Pretty print the dictionary to be displayed in the HTML pre tag
        introspection_details_json = json.dumps(introspection_details, indent=4)

        # Display the tokens and introspection details to the user
        return render_template_string(
            RESULT_PAGE_TEMPLATE,
            access_token=access_token,
            refresh_token=refresh_token,
            introspection_details=introspection_details_json
        )

    except Exception as e:
        # Catch any exceptions from the client library
        return f"An error occurred: {e}", 500

if __name__ == "__main__":
    # Run the Flask app in debug mode
    # For production, use a proper WSGI server like Gunicorn or uWSGI
    app.run(debug=True, port=8000, host="0.0.0.0")

