from kagglesdk.education.types.education_api_service import ApiTrackExerciseInteractionRequest, ApiTrackExerciseInteractionResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class EducationApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def track_exercise_interaction(self, request: ApiTrackExerciseInteractionRequest = None) -> ApiTrackExerciseInteractionResponse:
    r"""
    Args:
      request (ApiTrackExerciseInteractionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiTrackExerciseInteractionRequest()

    return self._client.call("education.EducationApiService", "TrackExerciseInteraction", request, ApiTrackExerciseInteractionResponse)
