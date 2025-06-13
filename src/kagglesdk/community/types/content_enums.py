import enum

class ContentState(enum.Enum):
  """Keep synced with /Kaggle.Sdk/cloud/kaggle/moderation/sor.proto"""
  CONTENT_STATE_UNSPECIFIED = 0
  PENDING_CLASSIFICATION = 1
  r"""
  Awaiting abuse classification. This exists as a non-visible state prior to
  classification.
  """
  PUBLISHED = 2
  r"""
  Publicly viewable, although access may be restricted outside of its content
  state.
  """
  TEMPORARILY_QUARANTINED = 3
  r"""
  Quarantined by an admin or by the system. This means that the content is
  only visible to the user and admins, however users are able to toggle their
  content out of this state.
  """
  PERMANENTLY_QUARANTINED = 4
  r"""
  Quarantined by an admin or by the system, the user cannot toggle their
  content's state back to public.
  """
  USER_DELETED = 5
  """Deleted by the user."""
  SYSTEM_DELETED = 6
  """Deleted by an admin or by a system account."""
  PENDING_PERMANENT_DELETE = 7
  """Awaiting hard deletion."""
  DRAFT = 8
  r"""
  Initial state of entity that has never been previously published.
  Unable to return back to Draft state once published.
  State flow chart example: http://screen/8vDypV7HPeuHBFK
  """
  UNPUBLISHED = 9
  r"""
  Intermediate stage that has either been upgraded from the Draft state or
  downgraded from the Published state.
  """

