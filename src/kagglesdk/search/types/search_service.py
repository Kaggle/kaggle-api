from datetime import datetime
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.discussions.types.writeup_enums import WriteUpType
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class WriteUpCompetitionInfo(KaggleObject):
  r"""
  Attributes:
    competition_title (str)
      Title of the Competition or Hackathon
    competition_url (str)
      Url of the Competition or Hackathon
    deadline (datetime)
      Deadline of the Competition or Hackathon
    write_up_leaderboard_rank (int)
      Rank of Competition Solution WriteUp on Leaderboard
    leaderboard_url (str)
      Leaderboard Tab Url for Competition
    winners_url (str)
      Winners Tab Url of Hackathon
    is_hackathon_winner (bool)
      Boolean to tell if user's WriteUp is winner of Hackathon
    competition_id (int)
      Id of the Competition
  """

  def __init__(self):
    self._competition_title = ""
    self._competition_url = ""
    self._deadline = None
    self._write_up_leaderboard_rank = None
    self._leaderboard_url = None
    self._winners_url = None
    self._is_hackathon_winner = None
    self._competition_id = 0
    self._freeze()

  @property
  def competition_title(self) -> str:
    """Title of the Competition or Hackathon"""
    return self._competition_title

  @competition_title.setter
  def competition_title(self, competition_title: str):
    if competition_title is None:
      del self.competition_title
      return
    if not isinstance(competition_title, str):
      raise TypeError('competition_title must be of type str')
    self._competition_title = competition_title

  @property
  def competition_url(self) -> str:
    """Url of the Competition or Hackathon"""
    return self._competition_url

  @competition_url.setter
  def competition_url(self, competition_url: str):
    if competition_url is None:
      del self.competition_url
      return
    if not isinstance(competition_url, str):
      raise TypeError('competition_url must be of type str')
    self._competition_url = competition_url

  @property
  def deadline(self) -> datetime:
    """Deadline of the Competition or Hackathon"""
    return self._deadline

  @deadline.setter
  def deadline(self, deadline: datetime):
    if deadline is None:
      del self.deadline
      return
    if not isinstance(deadline, datetime):
      raise TypeError('deadline must be of type datetime')
    self._deadline = deadline

  @property
  def write_up_leaderboard_rank(self) -> int:
    """Rank of Competition Solution WriteUp on Leaderboard"""
    return self._write_up_leaderboard_rank or 0

  @write_up_leaderboard_rank.setter
  def write_up_leaderboard_rank(self, write_up_leaderboard_rank: Optional[int]):
    if write_up_leaderboard_rank is None:
      del self.write_up_leaderboard_rank
      return
    if not isinstance(write_up_leaderboard_rank, int):
      raise TypeError('write_up_leaderboard_rank must be of type int')
    self._write_up_leaderboard_rank = write_up_leaderboard_rank

  @property
  def leaderboard_url(self) -> str:
    """Leaderboard Tab Url for Competition"""
    return self._leaderboard_url or ""

  @leaderboard_url.setter
  def leaderboard_url(self, leaderboard_url: Optional[str]):
    if leaderboard_url is None:
      del self.leaderboard_url
      return
    if not isinstance(leaderboard_url, str):
      raise TypeError('leaderboard_url must be of type str')
    self._leaderboard_url = leaderboard_url

  @property
  def winners_url(self) -> str:
    """Winners Tab Url of Hackathon"""
    return self._winners_url or ""

  @winners_url.setter
  def winners_url(self, winners_url: Optional[str]):
    if winners_url is None:
      del self.winners_url
      return
    if not isinstance(winners_url, str):
      raise TypeError('winners_url must be of type str')
    self._winners_url = winners_url

  @property
  def is_hackathon_winner(self) -> bool:
    """Boolean to tell if user's WriteUp is winner of Hackathon"""
    return self._is_hackathon_winner or False

  @is_hackathon_winner.setter
  def is_hackathon_winner(self, is_hackathon_winner: Optional[bool]):
    if is_hackathon_winner is None:
      del self.is_hackathon_winner
      return
    if not isinstance(is_hackathon_winner, bool):
      raise TypeError('is_hackathon_winner must be of type bool')
    self._is_hackathon_winner = is_hackathon_winner

  @property
  def competition_id(self) -> int:
    """Id of the Competition"""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class WriteUpItemInfo(KaggleObject):
  r"""
  Attributes:
    type (WriteUpType)
      Type of WriteUp
    subtitle (str)
      Subtitle of WriteUp
    collaborators (UserAvatar)
      List of WriteUp collaborators
    competition_info (WriteUpCompetitionInfo)
      Competition metadata associated with WriteUp
    content_state (ContentState)
      Content State of WriteUp
    team_name (str)
      Name of the team that owns the WriteUp
    id (int)
      Id of the WriteUp
  """

  def __init__(self):
    self._type = WriteUpType.WRITE_UP_TYPE_UNSPECIFIED
    self._subtitle = None
    self._collaborators = []
    self._competition_info = None
    self._content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._team_name = None
    self._id = 0
    self._freeze()

  @property
  def type(self) -> 'WriteUpType':
    """Type of WriteUp"""
    return self._type

  @type.setter
  def type(self, type: 'WriteUpType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, WriteUpType):
      raise TypeError('type must be of type WriteUpType')
    self._type = type

  @property
  def subtitle(self) -> str:
    """Subtitle of WriteUp"""
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: Optional[str]):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def collaborators(self) -> Optional[List[Optional['UserAvatar']]]:
    """List of WriteUp collaborators"""
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['UserAvatar']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, UserAvatar) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type UserAvatar')
    self._collaborators = collaborators

  @property
  def competition_info(self) -> Optional['WriteUpCompetitionInfo']:
    """Competition metadata associated with WriteUp"""
    return self._competition_info or None

  @competition_info.setter
  def competition_info(self, competition_info: Optional[Optional['WriteUpCompetitionInfo']]):
    if competition_info is None:
      del self.competition_info
      return
    if not isinstance(competition_info, WriteUpCompetitionInfo):
      raise TypeError('competition_info must be of type WriteUpCompetitionInfo')
    self._competition_info = competition_info

  @property
  def content_state(self) -> 'ContentState':
    """Content State of WriteUp"""
    return self._content_state

  @content_state.setter
  def content_state(self, content_state: 'ContentState'):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def team_name(self) -> str:
    """Name of the team that owns the WriteUp"""
    return self._team_name or ""

  @team_name.setter
  def team_name(self, team_name: Optional[str]):
    if team_name is None:
      del self.team_name
      return
    if not isinstance(team_name, str):
      raise TypeError('team_name must be of type str')
    self._team_name = team_name

  @property
  def id(self) -> int:
    """Id of the WriteUp"""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


WriteUpCompetitionInfo._fields = [
  FieldMetadata("competitionTitle", "competition_title", "_competition_title", str, "", PredefinedSerializer()),
  FieldMetadata("competitionUrl", "competition_url", "_competition_url", str, "", PredefinedSerializer()),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("writeUpLeaderboardRank", "write_up_leaderboard_rank", "_write_up_leaderboard_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("leaderboardUrl", "leaderboard_url", "_leaderboard_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("winnersUrl", "winners_url", "_winners_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isHackathonWinner", "is_hackathon_winner", "_is_hackathon_winner", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

WriteUpItemInfo._fields = [
  FieldMetadata("type", "type", "_type", WriteUpType, WriteUpType.WRITE_UP_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("collaborators", "collaborators", "_collaborators", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("competitionInfo", "competition_info", "_competition_info", WriteUpCompetitionInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

