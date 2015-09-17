# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyrnn.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyrnn.proto',
  package='kraken',
  serialized_pb=_b('\n\x0bpyrnn.proto\x12\x06kraken\"\'\n\x05\x61rray\x12\x0b\n\x03\x64im\x18\x01 \x03(\r\x12\x11\n\x05value\x18\x02 \x03(\x02\x42\x02\x10\x01\"\xca\x01\n\x04lstm\x12\x1a\n\x03wgi\x18\x01 \x02(\x0b\x32\r.kraken.array\x12\x1a\n\x03wgf\x18\x02 \x02(\x0b\x32\r.kraken.array\x12\x1a\n\x03wgo\x18\x03 \x02(\x0b\x32\r.kraken.array\x12\x1a\n\x03wci\x18\x04 \x02(\x0b\x32\r.kraken.array\x12\x1a\n\x03wip\x18\x05 \x02(\x0b\x32\r.kraken.array\x12\x1a\n\x03wfp\x18\x06 \x02(\x0b\x32\r.kraken.array\x12\x1a\n\x03wop\x18\x07 \x02(\x0b\x32\r.kraken.array\"$\n\x07softmax\x12\x19\n\x02w2\x18\x01 \x02(\x0b\x32\r.kraken.array\"\xb1\x01\n\x05pyrnn\x12\x0c\n\x04kind\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06ninput\x18\n \x02(\r\x12\x0f\n\x07noutput\x18\x0b \x02(\r\x12\r\n\x05\x63odec\x18\x0c \x03(\t\x12\x1c\n\x06\x66wdnet\x18\r \x02(\x0b\x32\x0c.kraken.lstm\x12\x1c\n\x06revnet\x18\x0e \x02(\x0b\x32\x0c.kraken.lstm\x12 \n\x07softmax\x18\x0f \x02(\x0b\x32\x0f.kraken.softmax')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ARRAY = _descriptor.Descriptor(
  name='array',
  full_name='kraken.array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim', full_name='kraken.array.dim', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='kraken.array.value', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=62,
)


_LSTM = _descriptor.Descriptor(
  name='lstm',
  full_name='kraken.lstm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wgi', full_name='kraken.lstm.wgi', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wgf', full_name='kraken.lstm.wgf', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wgo', full_name='kraken.lstm.wgo', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wci', full_name='kraken.lstm.wci', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wip', full_name='kraken.lstm.wip', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wfp', full_name='kraken.lstm.wfp', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wop', full_name='kraken.lstm.wop', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=267,
)


_SOFTMAX = _descriptor.Descriptor(
  name='softmax',
  full_name='kraken.softmax',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='w2', full_name='kraken.softmax.w2', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=305,
)


_PYRNN = _descriptor.Descriptor(
  name='pyrnn',
  full_name='kraken.pyrnn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='kraken.pyrnn.kind', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='kraken.pyrnn.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ninput', full_name='kraken.pyrnn.ninput', index=2,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noutput', full_name='kraken.pyrnn.noutput', index=3,
      number=11, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='codec', full_name='kraken.pyrnn.codec', index=4,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fwdnet', full_name='kraken.pyrnn.fwdnet', index=5,
      number=13, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revnet', full_name='kraken.pyrnn.revnet', index=6,
      number=14, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='softmax', full_name='kraken.pyrnn.softmax', index=7,
      number=15, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=485,
)

_LSTM.fields_by_name['wgi'].message_type = _ARRAY
_LSTM.fields_by_name['wgf'].message_type = _ARRAY
_LSTM.fields_by_name['wgo'].message_type = _ARRAY
_LSTM.fields_by_name['wci'].message_type = _ARRAY
_LSTM.fields_by_name['wip'].message_type = _ARRAY
_LSTM.fields_by_name['wfp'].message_type = _ARRAY
_LSTM.fields_by_name['wop'].message_type = _ARRAY
_SOFTMAX.fields_by_name['w2'].message_type = _ARRAY
_PYRNN.fields_by_name['fwdnet'].message_type = _LSTM
_PYRNN.fields_by_name['revnet'].message_type = _LSTM
_PYRNN.fields_by_name['softmax'].message_type = _SOFTMAX
DESCRIPTOR.message_types_by_name['array'] = _ARRAY
DESCRIPTOR.message_types_by_name['lstm'] = _LSTM
DESCRIPTOR.message_types_by_name['softmax'] = _SOFTMAX
DESCRIPTOR.message_types_by_name['pyrnn'] = _PYRNN

array = _reflection.GeneratedProtocolMessageType('array', (_message.Message,), dict(
  DESCRIPTOR = _ARRAY,
  __module__ = 'pyrnn_pb2'
  # @@protoc_insertion_point(class_scope:kraken.array)
  ))
_sym_db.RegisterMessage(array)

lstm = _reflection.GeneratedProtocolMessageType('lstm', (_message.Message,), dict(
  DESCRIPTOR = _LSTM,
  __module__ = 'pyrnn_pb2'
  # @@protoc_insertion_point(class_scope:kraken.lstm)
  ))
_sym_db.RegisterMessage(lstm)

softmax = _reflection.GeneratedProtocolMessageType('softmax', (_message.Message,), dict(
  DESCRIPTOR = _SOFTMAX,
  __module__ = 'pyrnn_pb2'
  # @@protoc_insertion_point(class_scope:kraken.softmax)
  ))
_sym_db.RegisterMessage(softmax)

pyrnn = _reflection.GeneratedProtocolMessageType('pyrnn', (_message.Message,), dict(
  DESCRIPTOR = _PYRNN,
  __module__ = 'pyrnn_pb2'
  # @@protoc_insertion_point(class_scope:kraken.pyrnn)
  ))
_sym_db.RegisterMessage(pyrnn)


_ARRAY.fields_by_name['value'].has_options = True
_ARRAY.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
