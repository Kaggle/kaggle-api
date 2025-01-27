import enum

class UserAchievementTier(enum.Enum):
  NOVICE = 0
  CONTRIBUTOR = 1
  EXPERT = 2
  MASTER = 3
  GRANDMASTER = 4
  STAFF = 5
  """Kaggle admins"""
  ORGANIZATION = 11
  """Organizations"""
  RECALC = 21
  """Flag user for tier recalculation"""

class CollaboratorType(enum.Enum):
  COLLABORATOR_TYPE_UNSPECIFIED = 0
  READER = 1
  WRITER = 2
  OWNER = 3
  ADMIN = 4

