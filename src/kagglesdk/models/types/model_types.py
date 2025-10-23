from datetime import datetime
from kagglesdk.datasets.types.dataset_enums import DatabundleVersionStatus, DatabundleVersionType
from kagglesdk.datasets.types.dataset_service import DatabundleVersionCreationStatus
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from kagglesdk.models.types.model_enums import ModelFramework, ModelInstanceType, ModelVersionLinkType, SigstoreState
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class BaseModelInstanceInformation(KaggleObject):
  r"""
  Attributes:
    id (int)
    owner (Owner)
    model_slug (str)
    instance_slug (str)
    framework (ModelFramework)
  """

  def __init__(self):
    self._id = 0
    self._owner = None
    self._model_slug = ""
    self._instance_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def owner(self) -> Optional['Owner']:
    return self._owner

  @owner.setter
  def owner(self, owner: Optional['Owner']):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, Owner):
      raise TypeError('owner must be of type Owner')
    self._owner = owner

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework


class LicensePost(KaggleObject):
  r"""
  Attributes:
    id (int)
    content (str)
  """

  def __init__(self):
    self._id = 0
    self._content = ""
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def content(self) -> str:
    return self._content

  @content.setter
  def content(self, content: str):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content


class ModelActivityTimeSeriesPoint(KaggleObject):
  r"""
  Attributes:
    date (datetime)
    count (int)
  """

  def __init__(self):
    self._date = None
    self._count = 0
    self._freeze()

  @property
  def date(self) -> datetime:
    return self._date

  @date.setter
  def date(self, date: datetime):
    if date is None:
      del self.date
      return
    if not isinstance(date, datetime):
      raise TypeError('date must be of type datetime')
    self._date = date

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class ModelInstance(KaggleObject):
  r"""
  Attributes:
    id (int)
    owner_slug (str)
    model_slug (str)
    slug (str)
    version_id (int)
    fine_tunable (bool)
    overview (str)
    usage (str)
    text_representation (str)
    source_url (str)
    version_number (int)
    framework (ModelFramework)
      TODO(http://b/253694274): Add support for variation tables when that's
      finished taking shape
    version_notes (str)
    download_url (str)
    databundle_version_id (int)
    last_version_id (int)
      Version ID associated with the most up-to-date version of the ModelInstance
    source_organization (Owner)
    training_data (str)
    metrics (str)
    license_post (LicensePost)
    rendered_usage (str)
    license (License)
    databundle_id (int)
    firestore_path (str)
    status (DatabundleVersionStatus)
    error_message (str)
    databundle_version_type (DatabundleVersionType)
    can_use (bool)
    creation_status (DatabundleVersionCreationStatus)
    uncompressed_storage_uri (str)
    model_instance_type (ModelInstanceType)
    base_model_instance_id (int)
    base_model_instance_information (BaseModelInstanceInformation)
    external_base_model_url (str)
    model_id (int)
    download_summary (ModelInstanceDownloadSummary)
    total_uncompressed_bytes (int)
    sigstore_state (SigstoreState)
    created_by_kernel_id (int)
    creator_user_id (int)
    attestation_kernel_url (str)
  """

  def __init__(self):
    self._id = 0
    self._owner_slug = ""
    self._model_slug = ""
    self._slug = ""
    self._version_id = 0
    self._fine_tunable = None
    self._overview = ""
    self._usage = ""
    self._text_representation = None
    self._source_url = None
    self._version_number = 0
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._version_notes = ""
    self._download_url = None
    self._databundle_version_id = 0
    self._last_version_id = None
    self._source_organization = None
    self._training_data = []
    self._metrics = None
    self._license_post = None
    self._rendered_usage = ""
    self._license = None
    self._databundle_id = 0
    self._firestore_path = ""
    self._status = DatabundleVersionStatus.NOT_YET_PERSISTED
    self._error_message = None
    self._databundle_version_type = DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED
    self._can_use = None
    self._creation_status = None
    self._uncompressed_storage_uri = None
    self._model_instance_type = None
    self._base_model_instance_id = None
    self._base_model_instance_information = None
    self._external_base_model_url = None
    self._model_id = 0
    self._download_summary = None
    self._total_uncompressed_bytes = None
    self._sigstore_state = None
    self._created_by_kernel_id = None
    self._creator_user_id = None
    self._attestation_kernel_url = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def model_id(self) -> int:
    return self._model_id

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def version_id(self) -> int:
    return self._version_id

  @version_id.setter
  def version_id(self, version_id: int):
    if version_id is None:
      del self.version_id
      return
    if not isinstance(version_id, int):
      raise TypeError('version_id must be of type int')
    self._version_id = version_id

  @property
  def fine_tunable(self) -> bool:
    return self._fine_tunable or False

  @fine_tunable.setter
  def fine_tunable(self, fine_tunable: Optional[bool]):
    if fine_tunable is None:
      del self.fine_tunable
      return
    if not isinstance(fine_tunable, bool):
      raise TypeError('fine_tunable must be of type bool')
    self._fine_tunable = fine_tunable

  @property
  def overview(self) -> str:
    return self._overview

  @overview.setter
  def overview(self, overview: str):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def usage(self) -> str:
    return self._usage

  @usage.setter
  def usage(self, usage: str):
    if usage is None:
      del self.usage
      return
    if not isinstance(usage, str):
      raise TypeError('usage must be of type str')
    self._usage = usage

  @property
  def rendered_usage(self) -> str:
    return self._rendered_usage

  @rendered_usage.setter
  def rendered_usage(self, rendered_usage: str):
    if rendered_usage is None:
      del self.rendered_usage
      return
    if not isinstance(rendered_usage, str):
      raise TypeError('rendered_usage must be of type str')
    self._rendered_usage = rendered_usage

  @property
  def text_representation(self) -> str:
    return self._text_representation or ""

  @text_representation.setter
  def text_representation(self, text_representation: Optional[str]):
    if text_representation is None:
      del self.text_representation
      return
    if not isinstance(text_representation, str):
      raise TypeError('text_representation must be of type str')
    self._text_representation = text_representation

  @property
  def source_url(self) -> str:
    return self._source_url or ""

  @source_url.setter
  def source_url(self, source_url: Optional[str]):
    if source_url is None:
      del self.source_url
      return
    if not isinstance(source_url, str):
      raise TypeError('source_url must be of type str')
    self._source_url = source_url

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def framework(self) -> 'ModelFramework':
    r"""
    TODO(http://b/253694274): Add support for variation tables when that's
    finished taking shape
    """
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def version_notes(self) -> str:
    return self._version_notes

  @version_notes.setter
  def version_notes(self, version_notes: str):
    if version_notes is None:
      del self.version_notes
      return
    if not isinstance(version_notes, str):
      raise TypeError('version_notes must be of type str')
    self._version_notes = version_notes

  @property
  def download_url(self) -> str:
    return self._download_url or ""

  @download_url.setter
  def download_url(self, download_url: Optional[str]):
    if download_url is None:
      del self.download_url
      return
    if not isinstance(download_url, str):
      raise TypeError('download_url must be of type str')
    self._download_url = download_url

  @property
  def databundle_id(self) -> int:
    return self._databundle_id

  @databundle_id.setter
  def databundle_id(self, databundle_id: int):
    if databundle_id is None:
      del self.databundle_id
      return
    if not isinstance(databundle_id, int):
      raise TypeError('databundle_id must be of type int')
    self._databundle_id = databundle_id

  @property
  def databundle_version_id(self) -> int:
    return self._databundle_version_id

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id

  @property
  def databundle_version_type(self) -> 'DatabundleVersionType':
    return self._databundle_version_type

  @databundle_version_type.setter
  def databundle_version_type(self, databundle_version_type: 'DatabundleVersionType'):
    if databundle_version_type is None:
      del self.databundle_version_type
      return
    if not isinstance(databundle_version_type, DatabundleVersionType):
      raise TypeError('databundle_version_type must be of type DatabundleVersionType')
    self._databundle_version_type = databundle_version_type

  @property
  def firestore_path(self) -> str:
    return self._firestore_path

  @firestore_path.setter
  def firestore_path(self, firestore_path: str):
    if firestore_path is None:
      del self.firestore_path
      return
    if not isinstance(firestore_path, str):
      raise TypeError('firestore_path must be of type str')
    self._firestore_path = firestore_path

  @property
  def status(self) -> 'DatabundleVersionStatus':
    return self._status

  @status.setter
  def status(self, status: 'DatabundleVersionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, DatabundleVersionStatus):
      raise TypeError('status must be of type DatabundleVersionStatus')
    self._status = status

  @property
  def creation_status(self) -> Optional['DatabundleVersionCreationStatus']:
    return self._creation_status or None

  @creation_status.setter
  def creation_status(self, creation_status: Optional[Optional['DatabundleVersionCreationStatus']]):
    if creation_status is None:
      del self.creation_status
      return
    if not isinstance(creation_status, DatabundleVersionCreationStatus):
      raise TypeError('creation_status must be of type DatabundleVersionCreationStatus')
    self._creation_status = creation_status

  @property
  def error_message(self) -> str:
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

  @property
  def last_version_id(self) -> int:
    """Version ID associated with the most up-to-date version of the ModelInstance"""
    return self._last_version_id or 0

  @last_version_id.setter
  def last_version_id(self, last_version_id: Optional[int]):
    if last_version_id is None:
      del self.last_version_id
      return
    if not isinstance(last_version_id, int):
      raise TypeError('last_version_id must be of type int')
    self._last_version_id = last_version_id

  @property
  def source_organization(self) -> Optional['Owner']:
    return self._source_organization or None

  @source_organization.setter
  def source_organization(self, source_organization: Optional[Optional['Owner']]):
    if source_organization is None:
      del self.source_organization
      return
    if not isinstance(source_organization, Owner):
      raise TypeError('source_organization must be of type Owner')
    self._source_organization = source_organization

  @property
  def training_data(self) -> Optional[List[str]]:
    return self._training_data

  @training_data.setter
  def training_data(self, training_data: Optional[List[str]]):
    if training_data is None:
      del self.training_data
      return
    if not isinstance(training_data, list):
      raise TypeError('training_data must be of type list')
    if not all([isinstance(t, str) for t in training_data]):
      raise TypeError('training_data must contain only items of type str')
    self._training_data = training_data

  @property
  def metrics(self) -> str:
    return self._metrics or ""

  @metrics.setter
  def metrics(self, metrics: Optional[str]):
    if metrics is None:
      del self.metrics
      return
    if not isinstance(metrics, str):
      raise TypeError('metrics must be of type str')
    self._metrics = metrics

  @property
  def license_post(self) -> Optional['LicensePost']:
    return self._license_post or None

  @license_post.setter
  def license_post(self, license_post: Optional[Optional['LicensePost']]):
    if license_post is None:
      del self.license_post
      return
    if not isinstance(license_post, LicensePost):
      raise TypeError('license_post must be of type LicensePost')
    self._license_post = license_post

  @property
  def license(self) -> Optional['License']:
    return self._license or None

  @license.setter
  def license(self, license: Optional[Optional['License']]):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def can_use(self) -> bool:
    return self._can_use or False

  @can_use.setter
  def can_use(self, can_use: Optional[bool]):
    if can_use is None:
      del self.can_use
      return
    if not isinstance(can_use, bool):
      raise TypeError('can_use must be of type bool')
    self._can_use = can_use

  @property
  def uncompressed_storage_uri(self) -> str:
    return self._uncompressed_storage_uri or ""

  @uncompressed_storage_uri.setter
  def uncompressed_storage_uri(self, uncompressed_storage_uri: Optional[str]):
    if uncompressed_storage_uri is None:
      del self.uncompressed_storage_uri
      return
    if not isinstance(uncompressed_storage_uri, str):
      raise TypeError('uncompressed_storage_uri must be of type str')
    self._uncompressed_storage_uri = uncompressed_storage_uri

  @property
  def model_instance_type(self) -> 'ModelInstanceType':
    return self._model_instance_type or ModelInstanceType.MODEL_INSTANCE_TYPE_UNSPECIFIED

  @model_instance_type.setter
  def model_instance_type(self, model_instance_type: Optional['ModelInstanceType']):
    if model_instance_type is None:
      del self.model_instance_type
      return
    if not isinstance(model_instance_type, ModelInstanceType):
      raise TypeError('model_instance_type must be of type ModelInstanceType')
    self._model_instance_type = model_instance_type

  @property
  def base_model_instance_id(self) -> int:
    return self._base_model_instance_id or 0

  @base_model_instance_id.setter
  def base_model_instance_id(self, base_model_instance_id: Optional[int]):
    if base_model_instance_id is None:
      del self.base_model_instance_id
      return
    if not isinstance(base_model_instance_id, int):
      raise TypeError('base_model_instance_id must be of type int')
    self._base_model_instance_id = base_model_instance_id

  @property
  def base_model_instance_information(self) -> Optional['BaseModelInstanceInformation']:
    return self._base_model_instance_information or None

  @base_model_instance_information.setter
  def base_model_instance_information(self, base_model_instance_information: Optional[Optional['BaseModelInstanceInformation']]):
    if base_model_instance_information is None:
      del self.base_model_instance_information
      return
    if not isinstance(base_model_instance_information, BaseModelInstanceInformation):
      raise TypeError('base_model_instance_information must be of type BaseModelInstanceInformation')
    self._base_model_instance_information = base_model_instance_information

  @property
  def external_base_model_url(self) -> str:
    return self._external_base_model_url or ""

  @external_base_model_url.setter
  def external_base_model_url(self, external_base_model_url: Optional[str]):
    if external_base_model_url is None:
      del self.external_base_model_url
      return
    if not isinstance(external_base_model_url, str):
      raise TypeError('external_base_model_url must be of type str')
    self._external_base_model_url = external_base_model_url

  @property
  def download_summary(self) -> Optional['ModelInstanceDownloadSummary']:
    return self._download_summary or None

  @download_summary.setter
  def download_summary(self, download_summary: Optional[Optional['ModelInstanceDownloadSummary']]):
    if download_summary is None:
      del self.download_summary
      return
    if not isinstance(download_summary, ModelInstanceDownloadSummary):
      raise TypeError('download_summary must be of type ModelInstanceDownloadSummary')
    self._download_summary = download_summary

  @property
  def total_uncompressed_bytes(self) -> int:
    return self._total_uncompressed_bytes or 0

  @total_uncompressed_bytes.setter
  def total_uncompressed_bytes(self, total_uncompressed_bytes: Optional[int]):
    if total_uncompressed_bytes is None:
      del self.total_uncompressed_bytes
      return
    if not isinstance(total_uncompressed_bytes, int):
      raise TypeError('total_uncompressed_bytes must be of type int')
    self._total_uncompressed_bytes = total_uncompressed_bytes

  @property
  def sigstore_state(self) -> 'SigstoreState':
    return self._sigstore_state or SigstoreState.SIGSTORE_STATE_UNSPECIFIED

  @sigstore_state.setter
  def sigstore_state(self, sigstore_state: Optional['SigstoreState']):
    if sigstore_state is None:
      del self.sigstore_state
      return
    if not isinstance(sigstore_state, SigstoreState):
      raise TypeError('sigstore_state must be of type SigstoreState')
    self._sigstore_state = sigstore_state

  @property
  def created_by_kernel_id(self) -> int:
    return self._created_by_kernel_id or 0

  @created_by_kernel_id.setter
  def created_by_kernel_id(self, created_by_kernel_id: Optional[int]):
    if created_by_kernel_id is None:
      del self.created_by_kernel_id
      return
    if not isinstance(created_by_kernel_id, int):
      raise TypeError('created_by_kernel_id must be of type int')
    self._created_by_kernel_id = created_by_kernel_id

  @property
  def creator_user_id(self) -> int:
    return self._creator_user_id or 0

  @creator_user_id.setter
  def creator_user_id(self, creator_user_id: Optional[int]):
    if creator_user_id is None:
      del self.creator_user_id
      return
    if not isinstance(creator_user_id, int):
      raise TypeError('creator_user_id must be of type int')
    self._creator_user_id = creator_user_id

  @property
  def attestation_kernel_url(self) -> str:
    return self._attestation_kernel_url or ""

  @attestation_kernel_url.setter
  def attestation_kernel_url(self, attestation_kernel_url: Optional[str]):
    if attestation_kernel_url is None:
      del self.attestation_kernel_url
      return
    if not isinstance(attestation_kernel_url, str):
      raise TypeError('attestation_kernel_url must be of type str')
    self._attestation_kernel_url = attestation_kernel_url


class ModelInstanceDownloadSummary(KaggleObject):
  r"""
  Attributes:
    total_downloads (float)
    download_series_points (ModelActivityTimeSeriesPoint)
    model_instance_id (int)
  """

  def __init__(self):
    self._total_downloads = 0.0
    self._download_series_points = []
    self._model_instance_id = 0
    self._freeze()

  @property
  def total_downloads(self) -> float:
    return self._total_downloads

  @total_downloads.setter
  def total_downloads(self, total_downloads: float):
    if total_downloads is None:
      del self.total_downloads
      return
    if not isinstance(total_downloads, float):
      raise TypeError('total_downloads must be of type float')
    self._total_downloads = total_downloads

  @property
  def download_series_points(self) -> Optional[List[Optional['ModelActivityTimeSeriesPoint']]]:
    return self._download_series_points

  @download_series_points.setter
  def download_series_points(self, download_series_points: Optional[List[Optional['ModelActivityTimeSeriesPoint']]]):
    if download_series_points is None:
      del self.download_series_points
      return
    if not isinstance(download_series_points, list):
      raise TypeError('download_series_points must be of type list')
    if not all([isinstance(t, ModelActivityTimeSeriesPoint) for t in download_series_points]):
      raise TypeError('download_series_points must contain only items of type ModelActivityTimeSeriesPoint')
    self._download_series_points = download_series_points

  @property
  def model_instance_id(self) -> int:
    return self._model_instance_id

  @model_instance_id.setter
  def model_instance_id(self, model_instance_id: int):
    if model_instance_id is None:
      del self.model_instance_id
      return
    if not isinstance(model_instance_id, int):
      raise TypeError('model_instance_id must be of type int')
    self._model_instance_id = model_instance_id


class ModelInstanceVersion(KaggleObject):
  r"""
  Attributes:
    id (int)
    framework (ModelFramework)
    is_tfhub_model (bool)
    url (str)
    variation_slug (str)
    version_number (int)
    model_title (str)
    thumbnail_url (str)
    is_private (bool)
    sigstore_state (SigstoreState)
  """

  def __init__(self):
    self._id = 0
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._is_tfhub_model = False
    self._url = ""
    self._variation_slug = ""
    self._version_number = 0
    self._model_title = ""
    self._thumbnail_url = ""
    self._is_private = False
    self._sigstore_state = SigstoreState.SIGSTORE_STATE_UNSPECIFIED
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def framework(self) -> 'ModelFramework':
    return self._framework

  @framework.setter
  def framework(self, framework: 'ModelFramework'):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def is_tfhub_model(self) -> bool:
    return self._is_tfhub_model

  @is_tfhub_model.setter
  def is_tfhub_model(self, is_tfhub_model: bool):
    if is_tfhub_model is None:
      del self.is_tfhub_model
      return
    if not isinstance(is_tfhub_model, bool):
      raise TypeError('is_tfhub_model must be of type bool')
    self._is_tfhub_model = is_tfhub_model

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def variation_slug(self) -> str:
    return self._variation_slug

  @variation_slug.setter
  def variation_slug(self, variation_slug: str):
    if variation_slug is None:
      del self.variation_slug
      return
    if not isinstance(variation_slug, str):
      raise TypeError('variation_slug must be of type str')
    self._variation_slug = variation_slug

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def model_title(self) -> str:
    return self._model_title

  @model_title.setter
  def model_title(self, model_title: str):
    if model_title is None:
      del self.model_title
      return
    if not isinstance(model_title, str):
      raise TypeError('model_title must be of type str')
    self._model_title = model_title

  @property
  def thumbnail_url(self) -> str:
    return self._thumbnail_url

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: str):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def sigstore_state(self) -> 'SigstoreState':
    return self._sigstore_state

  @sigstore_state.setter
  def sigstore_state(self, sigstore_state: 'SigstoreState'):
    if sigstore_state is None:
      del self.sigstore_state
      return
    if not isinstance(sigstore_state, SigstoreState):
      raise TypeError('sigstore_state must be of type SigstoreState')
    self._sigstore_state = sigstore_state


class ModelInstanceVersionList(KaggleObject):
  r"""
  Attributes:
    versions (ModelInstanceVersion)
  """

  def __init__(self):
    self._versions = []
    self._freeze()

  @property
  def versions(self) -> Optional[List[Optional['ModelInstanceVersion']]]:
    return self._versions

  @versions.setter
  def versions(self, versions: Optional[List[Optional['ModelInstanceVersion']]]):
    if versions is None:
      del self.versions
      return
    if not isinstance(versions, list):
      raise TypeError('versions must be of type list')
    if not all([isinstance(t, ModelInstanceVersion) for t in versions]):
      raise TypeError('versions must contain only items of type ModelInstanceVersion')
    self._versions = versions


class ModelLink(KaggleObject):
  r"""
  Attributes:
    type (ModelVersionLinkType)
    url (str)
  """

  def __init__(self):
    self._type = ModelVersionLinkType.MODEL_VERSION_LINK_TYPE_UNSPECIFIED
    self._url = ""
    self._freeze()

  @property
  def type(self) -> 'ModelVersionLinkType':
    return self._type

  @type.setter
  def type(self, type: 'ModelVersionLinkType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ModelVersionLinkType):
      raise TypeError('type must be of type ModelVersionLinkType')
    self._type = type

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class Owner(KaggleObject):
  r"""
  Based off Datasets OwnerDto as the permission model is the same
  Separate message since Models don't have max_file_size_bytes.
  Consider renaming more generically to apply to Users/Orgs
  interchangeably without a strict concept of ownership

  Attributes:
    id (int)
    image_url (str)
    is_organization (bool)
    name (str)
    profile_url (str)
    slug (str)
    user_tier (UserAchievementTier)
    allow_model_gating (bool)
    user_progression_opt_out (bool)
      Whether or not the owner is progression opted-out (only for user owners).
  """

  def __init__(self):
    self._id = 0
    self._image_url = None
    self._is_organization = False
    self._name = ""
    self._profile_url = None
    self._slug = ""
    self._user_tier = UserAchievementTier.NOVICE
    self._allow_model_gating = None
    self._user_progression_opt_out = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def image_url(self) -> str:
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: Optional[str]):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def is_organization(self) -> bool:
    return self._is_organization

  @is_organization.setter
  def is_organization(self, is_organization: bool):
    if is_organization is None:
      del self.is_organization
      return
    if not isinstance(is_organization, bool):
      raise TypeError('is_organization must be of type bool')
    self._is_organization = is_organization

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def profile_url(self) -> str:
    return self._profile_url or ""

  @profile_url.setter
  def profile_url(self, profile_url: Optional[str]):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def user_tier(self) -> 'UserAchievementTier':
    return self._user_tier

  @user_tier.setter
  def user_tier(self, user_tier: 'UserAchievementTier'):
    if user_tier is None:
      del self.user_tier
      return
    if not isinstance(user_tier, UserAchievementTier):
      raise TypeError('user_tier must be of type UserAchievementTier')
    self._user_tier = user_tier

  @property
  def user_progression_opt_out(self) -> bool:
    """Whether or not the owner is progression opted-out (only for user owners)."""
    return self._user_progression_opt_out or False

  @user_progression_opt_out.setter
  def user_progression_opt_out(self, user_progression_opt_out: Optional[bool]):
    if user_progression_opt_out is None:
      del self.user_progression_opt_out
      return
    if not isinstance(user_progression_opt_out, bool):
      raise TypeError('user_progression_opt_out must be of type bool')
    self._user_progression_opt_out = user_progression_opt_out

  @property
  def allow_model_gating(self) -> bool:
    return self._allow_model_gating or False

  @allow_model_gating.setter
  def allow_model_gating(self, allow_model_gating: Optional[bool]):
    if allow_model_gating is None:
      del self.allow_model_gating
      return
    if not isinstance(allow_model_gating, bool):
      raise TypeError('allow_model_gating must be of type bool')
    self._allow_model_gating = allow_model_gating


BaseModelInstanceInformation._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("owner", "owner", "_owner", Owner, None, KaggleObjectSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
]

LicensePost._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
]

ModelActivityTimeSeriesPoint._fields = [
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

ModelInstance._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionId", "version_id", "_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("fineTunable", "fine_tunable", "_fine_tunable", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("overview", "overview", "_overview", str, "", PredefinedSerializer()),
  FieldMetadata("usage", "usage", "_usage", str, "", PredefinedSerializer()),
  FieldMetadata("textRepresentation", "text_representation", "_text_representation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceUrl", "source_url", "_source_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, "", PredefinedSerializer()),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("lastVersionId", "last_version_id", "_last_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceOrganization", "source_organization", "_source_organization", Owner, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("trainingData", "training_data", "_training_data", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("metrics", "metrics", "_metrics", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licensePost", "license_post", "_license_post", LicensePost, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("renderedUsage", "rendered_usage", "_rendered_usage", str, "", PredefinedSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("databundleId", "databundle_id", "_databundle_id", int, 0, PredefinedSerializer()),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", DatabundleVersionStatus, DatabundleVersionStatus.NOT_YET_PERSISTED, EnumSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("databundleVersionType", "databundle_version_type", "_databundle_version_type", DatabundleVersionType, DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("canUse", "can_use", "_can_use", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationStatus", "creation_status", "_creation_status", DatabundleVersionCreationStatus, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("uncompressedStorageUri", "uncompressed_storage_uri", "_uncompressed_storage_uri", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceType", "model_instance_type", "_model_instance_type", ModelInstanceType, None, EnumSerializer(), optional=True),
  FieldMetadata("baseModelInstanceId", "base_model_instance_id", "_base_model_instance_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("baseModelInstanceInformation", "base_model_instance_information", "_base_model_instance_information", BaseModelInstanceInformation, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("externalBaseModelUrl", "external_base_model_url", "_external_base_model_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("downloadSummary", "download_summary", "_download_summary", ModelInstanceDownloadSummary, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("totalUncompressedBytes", "total_uncompressed_bytes", "_total_uncompressed_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sigstoreState", "sigstore_state", "_sigstore_state", SigstoreState, None, EnumSerializer(), optional=True),
  FieldMetadata("createdByKernelId", "created_by_kernel_id", "_created_by_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creatorUserId", "creator_user_id", "_creator_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("attestationKernelUrl", "attestation_kernel_url", "_attestation_kernel_url", str, None, PredefinedSerializer(), optional=True),
]

ModelInstanceDownloadSummary._fields = [
  FieldMetadata("totalDownloads", "total_downloads", "_total_downloads", float, 0.0, PredefinedSerializer()),
  FieldMetadata("downloadSeriesPoints", "download_series_points", "_download_series_points", ModelActivityTimeSeriesPoint, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("modelInstanceId", "model_instance_id", "_model_instance_id", int, 0, PredefinedSerializer()),
]

ModelInstanceVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isTfhubModel", "is_tfhub_model", "_is_tfhub_model", bool, False, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("variationSlug", "variation_slug", "_variation_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("modelTitle", "model_title", "_model_title", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, "", PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("sigstoreState", "sigstore_state", "_sigstore_state", SigstoreState, SigstoreState.SIGSTORE_STATE_UNSPECIFIED, EnumSerializer()),
]

ModelInstanceVersionList._fields = [
  FieldMetadata("versions", "versions", "_versions", ModelInstanceVersion, [], ListSerializer(KaggleObjectSerializer())),
]

ModelLink._fields = [
  FieldMetadata("type", "type", "_type", ModelVersionLinkType, ModelVersionLinkType.MODEL_VERSION_LINK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

Owner._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isOrganization", "is_organization", "_is_organization", bool, False, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("userTier", "user_tier", "_user_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("allowModelGating", "allow_model_gating", "_allow_model_gating", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userProgressionOptOut", "user_progression_opt_out", "_user_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
]

