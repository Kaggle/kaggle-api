import enum

class SearchUsersOrderBy(enum.Enum):
  SEARCH_USERS_ORDER_BY_UNSPECIFIED = 0
  SEARCH_USERS_ORDER_BY_COMPETITION_RANKING = 1
  """Ordered by current competition ranking, ascending (best rank first)."""
  SEARCH_USERS_ORDER_BY_KERNEL_RANKING = 2
  """Ordered by current kernel ranking, ascending (best rank first)."""
  SEARCH_USERS_ORDER_BY_DATASET_RANKING = 3
  """Ordered by current dataset ranking, ascending (best rank first)."""
  SEARCH_USERS_ORDER_BY_DISPLAY_NAME = 4
  """Ordered by display name, alphabetically, ascending."""
  SEARCH_USERS_ORDER_BY_TIER_AND_LEVEL = 5
  r"""
  Ordered by tier and tier levels, descending. Tier levels are awarded
  starting at Grandmaster. The first user returned will have the highest tier
  and level (GM 7x, etc.).
  """
  SEARCH_USERS_ORDER_BY_OLDEST_JOIN_DATE = 6
  """Ordered by user create date, ascending (i.e. oldest account first)."""
  SEARCH_USERS_ORDER_BY_NEWEST_JOIN_DATE = 7
  """Ordered by user create date, descending (i.e. newest account first)."""

