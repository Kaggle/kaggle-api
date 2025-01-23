import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class LearnExerciseInteractionType(enum.Enum):
  LEARN_EXERCISE_INTERACTION_TYPE_UNSPECIFIED = 0
  CHECK = 1
  HINT = 2
  SOLUTION = 3

class LearnExerciseOutcomeType(enum.Enum):
  LEARN_EXERCISE_OUTCOME_TYPE_UNSPECIFIED = 0
  PASS = 1
  FAIL = 2
  EXCEPTION = 3
  UNATTEMPTED = 4

class LearnExerciseQuestionType(enum.Enum):
  LEARN_EXERCISE_QUESTION_TYPE_UNSPECIFIED = 0
  EQUALITY_CHECK_PROBLEM = 1
  CODING_PROBLEM = 2
  FUNCTION_PROBLEM = 3
  THOUGHT_EXPERIMENT = 4

class LearnNudgeType(enum.Enum):
  COURSE_COMPLETE_NO_BONUS_LESSONS = 0
  COURSE_COMPLETE_WITH_BONUS_LESSONS = 1
  COURSE_INCOMPLETE = 2
  DO_EXERCISE = 3
  DO_TUTORIAL = 4

class LearnNudge(KaggleObject):
  r"""
  Attributes:
    course_index (int)
    course_name (str)
    course_slug (str)
    next_item_name (str)
    next_item_url (str)
    next_item_type (LearnNudgeType)
  """

  def __init__(self):
    self._course_index = 0
    self._course_name = ""
    self._course_slug = ""
    self._next_item_name = ""
    self._next_item_url = ""
    self._next_item_type = LearnNudgeType.COURSE_COMPLETE_NO_BONUS_LESSONS
    self._freeze()

  @property
  def course_index(self) -> int:
    return self._course_index

  @course_index.setter
  def course_index(self, course_index: int):
    if course_index is None:
      del self.course_index
      return
    if not isinstance(course_index, int):
      raise TypeError('course_index must be of type int')
    self._course_index = course_index

  @property
  def course_name(self) -> str:
    return self._course_name

  @course_name.setter
  def course_name(self, course_name: str):
    if course_name is None:
      del self.course_name
      return
    if not isinstance(course_name, str):
      raise TypeError('course_name must be of type str')
    self._course_name = course_name

  @property
  def course_slug(self) -> str:
    return self._course_slug

  @course_slug.setter
  def course_slug(self, course_slug: str):
    if course_slug is None:
      del self.course_slug
      return
    if not isinstance(course_slug, str):
      raise TypeError('course_slug must be of type str')
    self._course_slug = course_slug

  @property
  def next_item_name(self) -> str:
    return self._next_item_name

  @next_item_name.setter
  def next_item_name(self, next_item_name: str):
    if next_item_name is None:
      del self.next_item_name
      return
    if not isinstance(next_item_name, str):
      raise TypeError('next_item_name must be of type str')
    self._next_item_name = next_item_name

  @property
  def next_item_url(self) -> str:
    return self._next_item_url

  @next_item_url.setter
  def next_item_url(self, next_item_url: str):
    if next_item_url is None:
      del self.next_item_url
      return
    if not isinstance(next_item_url, str):
      raise TypeError('next_item_url must be of type str')
    self._next_item_url = next_item_url

  @property
  def next_item_type(self) -> 'LearnNudgeType':
    return self._next_item_type

  @next_item_type.setter
  def next_item_type(self, next_item_type: 'LearnNudgeType'):
    if next_item_type is None:
      del self.next_item_type
      return
    if not isinstance(next_item_type, LearnNudgeType):
      raise TypeError('next_item_type must be of type LearnNudgeType')
    self._next_item_type = next_item_type


LearnNudge._fields = [
  FieldMetadata("courseIndex", "course_index", "_course_index", int, 0, PredefinedSerializer()),
  FieldMetadata("courseName", "course_name", "_course_name", str, "", PredefinedSerializer()),
  FieldMetadata("courseSlug", "course_slug", "_course_slug", str, "", PredefinedSerializer()),
  FieldMetadata("nextItemName", "next_item_name", "_next_item_name", str, "", PredefinedSerializer()),
  FieldMetadata("nextItemUrl", "next_item_url", "_next_item_url", str, "", PredefinedSerializer()),
  FieldMetadata("nextItemType", "next_item_type", "_next_item_type", LearnNudgeType, LearnNudgeType.COURSE_COMPLETE_NO_BONUS_LESSONS, EnumSerializer()),
]

