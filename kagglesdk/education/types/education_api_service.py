from kagglesdk.education.types.education_service import LearnExerciseInteractionType, LearnExerciseOutcomeType, LearnExerciseQuestionType, LearnNudge
from kagglesdk.kaggle_object import *
from typing import Optional

class ApiTrackExerciseInteractionRequest(KaggleObject):
  r"""
  This is copied from TrackExerciseInteractionRequest in
  education_service.proto, which will eventually be deprecated.  In the
  meantime, make sure to keep these in sync.

  NOTE: there's one small rename from `fork_parent_script_version_id` to
  `fork_parent_kernel_session_id`.

  Attributes:
    exception_class (str)
    failure_message (str)
    interaction_type (LearnExerciseInteractionType)
    learn_tools_version (str)
    fork_parent_kernel_session_id (int)
    outcome_type (LearnExerciseOutcomeType)
    question_id (str)
    question_type (LearnExerciseQuestionType)
    trace (str)
    value_towards_completion (float)
  """

  def __init__(self):
    self._exception_class = ""
    self._failure_message = ""
    self._interaction_type = LearnExerciseInteractionType.LEARN_EXERCISE_INTERACTION_TYPE_UNSPECIFIED
    self._learn_tools_version = ""
    self._fork_parent_kernel_session_id = 0
    self._outcome_type = LearnExerciseOutcomeType.LEARN_EXERCISE_OUTCOME_TYPE_UNSPECIFIED
    self._question_id = ""
    self._question_type = LearnExerciseQuestionType.LEARN_EXERCISE_QUESTION_TYPE_UNSPECIFIED
    self._trace = ""
    self._value_towards_completion = None
    self._freeze()

  @property
  def exception_class(self) -> str:
    return self._exception_class

  @exception_class.setter
  def exception_class(self, exception_class: str):
    if exception_class is None:
      del self.exception_class
      return
    if not isinstance(exception_class, str):
      raise TypeError('exception_class must be of type str')
    self._exception_class = exception_class

  @property
  def failure_message(self) -> str:
    return self._failure_message

  @failure_message.setter
  def failure_message(self, failure_message: str):
    if failure_message is None:
      del self.failure_message
      return
    if not isinstance(failure_message, str):
      raise TypeError('failure_message must be of type str')
    self._failure_message = failure_message

  @property
  def interaction_type(self) -> 'LearnExerciseInteractionType':
    return self._interaction_type

  @interaction_type.setter
  def interaction_type(self, interaction_type: 'LearnExerciseInteractionType'):
    if interaction_type is None:
      del self.interaction_type
      return
    if not isinstance(interaction_type, LearnExerciseInteractionType):
      raise TypeError('interaction_type must be of type LearnExerciseInteractionType')
    self._interaction_type = interaction_type

  @property
  def learn_tools_version(self) -> str:
    return self._learn_tools_version

  @learn_tools_version.setter
  def learn_tools_version(self, learn_tools_version: str):
    if learn_tools_version is None:
      del self.learn_tools_version
      return
    if not isinstance(learn_tools_version, str):
      raise TypeError('learn_tools_version must be of type str')
    self._learn_tools_version = learn_tools_version

  @property
  def fork_parent_kernel_session_id(self) -> int:
    return self._fork_parent_kernel_session_id

  @fork_parent_kernel_session_id.setter
  def fork_parent_kernel_session_id(self, fork_parent_kernel_session_id: int):
    if fork_parent_kernel_session_id is None:
      del self.fork_parent_kernel_session_id
      return
    if not isinstance(fork_parent_kernel_session_id, int):
      raise TypeError('fork_parent_kernel_session_id must be of type int')
    self._fork_parent_kernel_session_id = fork_parent_kernel_session_id

  @property
  def outcome_type(self) -> 'LearnExerciseOutcomeType':
    return self._outcome_type

  @outcome_type.setter
  def outcome_type(self, outcome_type: 'LearnExerciseOutcomeType'):
    if outcome_type is None:
      del self.outcome_type
      return
    if not isinstance(outcome_type, LearnExerciseOutcomeType):
      raise TypeError('outcome_type must be of type LearnExerciseOutcomeType')
    self._outcome_type = outcome_type

  @property
  def question_id(self) -> str:
    return self._question_id

  @question_id.setter
  def question_id(self, question_id: str):
    if question_id is None:
      del self.question_id
      return
    if not isinstance(question_id, str):
      raise TypeError('question_id must be of type str')
    self._question_id = question_id

  @property
  def question_type(self) -> 'LearnExerciseQuestionType':
    return self._question_type

  @question_type.setter
  def question_type(self, question_type: 'LearnExerciseQuestionType'):
    if question_type is None:
      del self.question_type
      return
    if not isinstance(question_type, LearnExerciseQuestionType):
      raise TypeError('question_type must be of type LearnExerciseQuestionType')
    self._question_type = question_type

  @property
  def trace(self) -> str:
    return self._trace

  @trace.setter
  def trace(self, trace: str):
    if trace is None:
      del self.trace
      return
    if not isinstance(trace, str):
      raise TypeError('trace must be of type str')
    self._trace = trace

  @property
  def value_towards_completion(self) -> float:
    return self._value_towards_completion or 0.0

  @value_towards_completion.setter
  def value_towards_completion(self, value_towards_completion: float):
    if value_towards_completion is None:
      del self.value_towards_completion
      return
    if not isinstance(value_towards_completion, float):
      raise TypeError('value_towards_completion must be of type float')
    self._value_towards_completion = value_towards_completion

  def endpoint(self):
    path = '/api/v1/learn/track'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiTrackExerciseInteractionResponse(KaggleObject):
  r"""
  This is copied from TrackExerciseInteractionResponse in
  education_service.proto, which will eventually be deprecated.  In the
  meantime, make sure to keep these in sync.

  Attributes:
    nudge (LearnNudge)
    show_login_prompt (bool)
  """

  def __init__(self):
    self._nudge = None
    self._show_login_prompt = False
    self._freeze()

  @property
  def nudge(self) -> Optional['LearnNudge']:
    return self._nudge

  @nudge.setter
  def nudge(self, nudge: Optional['LearnNudge']):
    if nudge is None:
      del self.nudge
      return
    if not isinstance(nudge, LearnNudge):
      raise TypeError('nudge must be of type LearnNudge')
    self._nudge = nudge

  @property
  def show_login_prompt(self) -> bool:
    return self._show_login_prompt

  @show_login_prompt.setter
  def show_login_prompt(self, show_login_prompt: bool):
    if show_login_prompt is None:
      del self.show_login_prompt
      return
    if not isinstance(show_login_prompt, bool):
      raise TypeError('show_login_prompt must be of type bool')
    self._show_login_prompt = show_login_prompt

  @property
  def showLoginPrompt(self):
    return self.show_login_prompt


ApiTrackExerciseInteractionRequest._fields = [
  FieldMetadata("exceptionClass", "exception_class", "_exception_class", str, "", PredefinedSerializer()),
  FieldMetadata("failureMessage", "failure_message", "_failure_message", str, "", PredefinedSerializer()),
  FieldMetadata("interactionType", "interaction_type", "_interaction_type", LearnExerciseInteractionType, LearnExerciseInteractionType.LEARN_EXERCISE_INTERACTION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("learnToolsVersion", "learn_tools_version", "_learn_tools_version", str, "", PredefinedSerializer()),
  FieldMetadata("forkParentKernelSessionId", "fork_parent_kernel_session_id", "_fork_parent_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("outcomeType", "outcome_type", "_outcome_type", LearnExerciseOutcomeType, LearnExerciseOutcomeType.LEARN_EXERCISE_OUTCOME_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("questionId", "question_id", "_question_id", str, "", PredefinedSerializer()),
  FieldMetadata("questionType", "question_type", "_question_type", LearnExerciseQuestionType, LearnExerciseQuestionType.LEARN_EXERCISE_QUESTION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("trace", "trace", "_trace", str, "", PredefinedSerializer()),
  FieldMetadata("valueTowardsCompletion", "value_towards_completion", "_value_towards_completion", float, None, PredefinedSerializer(), optional=True),
]

ApiTrackExerciseInteractionResponse._fields = [
  FieldMetadata("nudge", "nudge", "_nudge", LearnNudge, None, KaggleObjectSerializer()),
  FieldMetadata("showLoginPrompt", "show_login_prompt", "_show_login_prompt", bool, False, PredefinedSerializer()),
]

