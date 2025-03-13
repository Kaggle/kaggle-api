import json
import re
from datetime import datetime, timedelta
from google.protobuf.field_mask_pb2 import FieldMask


class ObjectSerializer(object):
  def __init__(self, to_dict_value, from_dict_value):
    self.to_dict_value = to_dict_value
    self.from_dict_value = from_dict_value


class PredefinedSerializer(ObjectSerializer):
  def __init__(self):
    """Predefined objects such as int, float etc are serialized/deserialized directly."""
    ObjectSerializer.__init__(self, lambda cls, v, _: v, lambda cls, v: v)


# Adapted from https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
_pascal_to_upper_snake_case_regex = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')


def _pascal_case_to_upper_snake_case(string):
  return _pascal_to_upper_snake_case_regex.sub(r'_\1', string).upper()


def _convert (camel_input):
  words = re.findall(r'[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+', camel_input)
  return '_'.join(map(str.lower, words))


class EnumSerializer(ObjectSerializer):
  def __init__(self):
    """
    Enum objects are serialized using their ".name" field and deserialized by indexing the string in the Enum type.
    Example:
    class Foo(Enum):
       TEST = 1
    foo = Foo.TEST
    foo.name # => returns "TEST"
    Foo["TEST"] # => returns Foo.TEST enum value.
    """
    ObjectSerializer.__init__(self,
                              lambda cls, v, _: EnumSerializer._to_str(cls, v),
                              lambda cls, v: EnumSerializer._from_str(cls, v))

  @staticmethod
  def _to_str(cls, v):
    # "v" corresponds to an enum instance: Example foo or Foo.Test above.
    # "cls" corresponds to the enum type Foo above.
    #enum_prefix = f'{_pascal_case_to_upper_snake_case(cls.__name__)}_'
    #if v.name.startswith(enum_prefix):
    #  return v.name
    #return f'{enum_prefix}{v.name}'
    enum_prefix = f'{_pascal_case_to_upper_snake_case(cls.__name__)}_'
    if v.name.find(enum_prefix) == 0:
      return v.name[len(enum_prefix):].lower()
    return v.name

  @staticmethod
  def _from_str(cls, v):
    # "v" corresponds to enum string: Example "TEST" above.
    # "cls" corresponds to the enum type Foo above.
    # enum_items = {item.name: item for item in cls}
    # if v in enum_items:
    #   return enum_items[v]
    # 
    # # Try with enum prefix. Example: EnvironmentType.JSON -> "ENVIRONMENT_TYPE_JSON"
    # enum_prefix = _pascal_case_to_upper_snake_case(cls.__name__)
    # if v.startswith(enum_prefix):
    #   ix_start = len(enum_prefix) + 1
    #   return enum_items[v[ix_start:]]
    # 
    # return enum_items[f'{enum_prefix}_{v}']
    try:
      return cls[v]
    except KeyError:
      dct = vars(cls)
      n = v.lower()
      nn = _convert(v).lower()
      enum_prefix = _pascal_case_to_upper_snake_case(cls.__name__).lower()
      for key in dct.keys():
        k = key.lower()
        if k == n:
          return dct[key]
        if k.startswith(enum_prefix) and k.endswith(n) or k.endswith(nn):
          return dct[key]
      raise


class ListSerializer(ObjectSerializer):
  def __init__(self, item_serializer: ObjectSerializer):
    """
    Lists are serialized based on the type they contain. Since objects are generated from proto files, a list always
    contains objects of the same type, which is serialized/deserialized using "item_serializer".
    """
    ObjectSerializer.__init__(self,
                              lambda cls, l, ignore_defaults: [item_serializer.to_dict_value(cls, v, ignore_defaults) for v in l],
                              lambda cls, l: [item_serializer.from_dict_value(cls, v) for v in l])


class MapSerializer(ObjectSerializer):
  def __init__(self, item_serializer: ObjectSerializer):
    """
    Maps are serialized based on type of their values. Since maps keys are always predefined types, we don't need a
    serializer for them.
    """
    ObjectSerializer.__init__(self,
                              lambda cls, d, ignore_defaults: {k: item_serializer.to_dict_value(cls, v, ignore_defaults) for k, v in d.items()},
                              lambda cls, d: {k: item_serializer.from_dict_value(cls, v) for k, v in d.items()})


class DateTimeSerializer(ObjectSerializer):
  def __init__(self):
    """Date times are serialized/deserialized as a string in iso format"""
    ObjectSerializer.__init__(self,
                              lambda cls, dt, _: DateTimeSerializer._to_str(dt),
                              lambda _, v: DateTimeSerializer._from_str(v))

  @staticmethod
  def _to_str(dt):
    return dt.isoformat(timespec='milliseconds') + 'Z'

  @staticmethod
  def _from_str(v):
    v = v.rstrip('Z')
    fields = v.rsplit('.', maxsplit=1)
    if len(fields) == 1:
      return datetime.fromisoformat(v)
    (dt, nanos) = fields
    millis = nanos[:3]
    try:
      return datetime.fromisoformat(f'{dt}.{millis}')
    except ValueError:
      return datetime.fromisoformat(dt) # Python 3.9, 3.10


class TimeDeltaSerializer(ObjectSerializer):
  def __init__(self):
    """Time deltas are serialized/deserialized as a string in "mm:ss" format"""
    ObjectSerializer.__init__(self,
                              lambda cls, t, _: TimeDeltaSerializer._to_dict_value(t),
                              lambda cls, v: TimeDeltaSerializer._from_dict_value(v))

  @staticmethod
  def _to_dict_value(delta):
    seconds = int(delta.total_seconds())
    minutes = seconds // 60
    seconds -= minutes * 60
    return '{}:{:02}'.format(int(minutes), int(seconds))

  @staticmethod
  def _from_dict_value(value):
    (minutes, seconds) = value.split(':')
    return timedelta(minutes=int(minutes), seconds=int(seconds))


class FieldMaskSerializer(ObjectSerializer):
  def __init__(self):
    """Field masks are serialized/deserialized as a string that contains a list of paths with a comma delimiter"""
    ObjectSerializer.__init__(self,
                              lambda cls, m, _: m.ToJsonString(),
                              lambda cls, v: FieldMaskSerializer._from_joined_paths(v))

  @staticmethod
  def _from_joined_paths(joined_paths):
    mask = FieldMask()
    mask.FromJsonString(joined_paths)
    return mask


class KaggleObjectSerializer(ObjectSerializer):
  def __init__(self):
    """
    Kaggle objects (i.e., proto-generated types that inherit from KaggleObject) have custom "to_dict" and "from_dict"
    methods that serialize/deserialize them to/from dictionaries.
    """
    ObjectSerializer.__init__(self,
                              # "v" is an instance of a KaggleObject. For example: "req = ListCompetitionsRequest()".
                              # So "req.to_dict()" returns a dictionary with keys as json field names. Example:
                              # '{"pageSize": 10, "page": 2}'
                              lambda cls, v, ignore_defaults: cls.to_dict(v, ignore_defaults),
                              # "cls" is the type of a KaggleObject. For example: ListCompetitionsRequest. All
                              # generated Kaggle objects have "from_dict" class method that takes a dict to create a
                              # new instance of the object. See "KaggleObject" class definition below.
                              lambda cls, v: cls.from_dict(v))


class FieldMetadata(object):
  def __init__(self, json_name, field_name, private_field_name, field_type, default_value, serializer, optional=False):
    self.json_name = json_name
    self.field_name = field_name
    self.private_field_name = private_field_name
    self.field_type = field_type
    self.default_value = default_value
    self.serializer = serializer
    self.optional = optional

  def get_as_dict_item(self, instance, ignore_defaults=True):
    value = getattr(instance, self.private_field_name)
    if ignore_defaults and value == self.default_value:
      return None
    if value is None:
      return None
    return self.serializer.to_dict_value(self.field_type, value, ignore_defaults)

  def set_from_dict(self, instance, json_dict):
    if self.json_name not in json_dict:
      return  # Ignore unknown fields
    value = json_dict[self.json_name]
    if value == self.default_value:
      return  # Ignore default values
    try:
      setattr(instance, self.private_field_name, self.serializer.from_dict_value(self.field_type, value))
    except Exception as e:
      raise


class KaggleObject(object):
  def endpoint(self):
    raise 'Error: endpoint must be defined by the request object'

  @staticmethod
  def endpoint_path():
    return None

  @staticmethod
  def body_fields():
    return None

  @classmethod
  def prepare_from(cls, http_response):
    return cls.from_json(http_response.text)

  @staticmethod
  def method():
    return "GET"

  def _freeze(self):
    self._is_frozen = True

  def __setattr__(self, key, value):
    if hasattr(self, '_is_frozen') and not hasattr(self, key):
      raise AttributeError(f'Unknown field for {self.__class__.__name__}: {key}')
    object.__setattr__(self, key, value)

  def to_dict(self, ignore_defaults=True):
    kv_pairs = [(field.json_name, field.get_as_dict_item(self, ignore_defaults)) for field in self._fields]
    return {k: v for (k, v) in kv_pairs if not ignore_defaults or v is not None}

  @staticmethod
  def to_field_map(self, ignore_defaults=True):
    kv_pairs = [(field.field_name, field.get_as_dict_item(self, ignore_defaults)) for field in self._fields]
    return {k: v for (k, v) in kv_pairs if not ignore_defaults or v is not None}

  @classmethod
  def from_dict(cls, json_dict):
    instance = cls()
    for field in cls._fields:
      field.set_from_dict(instance, json_dict)
    return instance

  @classmethod
  def from_json(cls, json_str):
    return cls.from_dict(json.loads(json_str))

  @staticmethod
  def to_json(self, ignore_defaults=True):
    return json.dumps(KaggleObject.to_dict(self, ignore_defaults))

  def __str__(self):
    return KaggleObject.to_json(self, ignore_defaults=False)

  def __repr__(self):
    return KaggleObject.to_json(self, ignore_defaults=False)

  def __contains__(self, field_name):
    try:
      field = self._get_field(field_name)
    except ValueError:
      return False
    value = getattr(self, field.private_field_name)
    if field.optional:
      return value is not None
    else:
      return value != field.default_value

  def __delattr__(self, field_name):
    field = self._get_field(field_name)
    setattr(self, field.private_field_name, field.default_value)

  def _get_field(self, field_name):
    field = next((f for f in self._fields if f.field_name == field_name), None)
    if field is None:
      raise ValueError(f'Protocol message {self.__class__.__name__} has no "{field_name}" field.')
    return field
