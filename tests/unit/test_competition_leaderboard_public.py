# coding=utf-8
import sys
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, "../..")

from kaggle.api.kaggle_api_extended import KaggleApi


class _LeaderboardTestCase(unittest.TestCase):
    """Shared setup for competition_leaderboard_view and its CLI wrapper."""

    def setUp(self):
        self.api = KaggleApi.__new__(KaggleApi)
        self.api.config_values = {}

    def _patch_client(self, mock_client):
        mock_kaggle = MagicMock()
        response = MagicMock()
        response.submissions = []
        response.next_page_token = ""
        mock_kaggle.competitions.competition_api_client.get_leaderboard.return_value = response
        mock_client.return_value.__enter__ = MagicMock(return_value=mock_kaggle)
        mock_client.return_value.__exit__ = MagicMock(return_value=False)
        return mock_kaggle

    @staticmethod
    def _sent(mock_kaggle):
        return mock_kaggle.competitions.competition_api_client.get_leaderboard.call_args[0][0]


class TestLeaderboardPublicFlag(_LeaderboardTestCase):

    @patch.object(KaggleApi, "build_kaggle_client")
    def test_public_sets_override_public(self, mock_client):
        mock_kaggle = self._patch_client(mock_client)

        self.api.competition_leaderboard_view("my-comp", public=True)

        request = self._sent(mock_kaggle)
        self.assertEqual(request.competition_name, "my-comp")
        self.assertTrue(request.override_public)

    @patch.object(KaggleApi, "build_kaggle_client")
    def test_default_leaves_the_request_unchanged(self, mock_client):
        # Not setting the field is what gets the final leaderboard, so the default must not change.
        mock_kaggle = self._patch_client(mock_client)

        self.api.competition_leaderboard_view("my-comp")

        self.assertFalse(self._sent(mock_kaggle).override_public)

    @patch.object(KaggleApi, "build_kaggle_client")
    def test_public_false_leaves_the_request_unchanged(self, mock_client):
        mock_kaggle = self._patch_client(mock_client)

        self.api.competition_leaderboard_view("my-comp", public=False)

        self.assertFalse(self._sent(mock_kaggle).override_public)

    @patch.object(KaggleApi, "build_kaggle_client")
    def test_paging_still_applies_with_public(self, mock_client):
        mock_kaggle = self._patch_client(mock_client)

        self.api.competition_leaderboard_view("my-comp", 50, "a-token", True)

        request = self._sent(mock_kaggle)
        self.assertTrue(request.override_public)
        self.assertEqual(request.page_size, 50)
        self.assertEqual(request.page_token, "a-token")


class TestLeaderboardCliForwardsPublic(_LeaderboardTestCase):

    @patch.object(KaggleApi, "competition_leaderboard_view")
    def test_cli_forwards_public_to_view(self, mock_view):
        mock_view.return_value = []

        self.api.competition_leaderboard_cli("my-comp", view=True, public=True)

        self.assertIs(mock_view.call_args[0][3], True)

    @patch.object(KaggleApi, "competition_leaderboard_view")
    def test_cli_defaults_to_the_final_leaderboard(self, mock_view):
        mock_view.return_value = []

        self.api.competition_leaderboard_cli("my-comp", view=True)

        self.assertIs(mock_view.call_args[0][3], False)

    @patch.object(KaggleApi, "competition_leaderboard_download")
    def test_public_does_not_reach_the_download_path(self, mock_download):
        # DownloadLeaderboard has no override field, so --public must not alter the call.
        self.api.competition_leaderboard_cli("my-comp", download=True, public=True)

        mock_download.assert_called_once_with("my-comp", None, False)


if __name__ == "__main__":
    unittest.main()
