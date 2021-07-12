# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\nuser/proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nuser.proto\x1a\x1bgoogle/protobuf/empty.proto\"%\n\x08PageInfo\x12\n\n\x02pn\x18\x01 \x01(\r\x12\r\n\x05pSize\x18\x02 \x01(\r\"\x1f\n\rMobileRequest\x12\x0e\n\x06mobile\x18\x01 \x01(\t\"D\n\x0e\x43reateUserInfo\x12\x10\n\x08nickName\x18\x01 \x01(\t\x12\x10\n\x08passWord\x18\x02 \x01(\t\x12\x0e\n\x06mobile\x18\x03 \x01(\t\"P\n\x0eUpdateUserInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08nickName\x18\x02 \x01(\t\x12\x0e\n\x06gender\x18\x03 \x01(\t\x12\x10\n\x08\x62irthDay\x18\x04 \x01(\x04\"\x0b\n\tIdRequest\"\x82\x01\n\x10UserInfoResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08passWord\x18\x02 \x01(\t\x12\x0e\n\x06mobile\x18\x03 \x01(\t\x12\x10\n\x08nickName\x18\x04 \x01(\t\x12\x10\n\x08\x62irthDay\x18\x05 \x01(\x04\x12\x0e\n\x06gender\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\x05\"B\n\x10UserListResponse\x12\r\n\x05total\x18\x01 \x01(\r\x12\x1f\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x11.UserInfoResponse2\x80\x02\n\x04User\x12+\n\x0bGetUserList\x12\t.PageInfo\x1a\x11.UserListResponse\x12\x34\n\x0fGetUserByMobile\x12\x0e.MobileRequest\x1a\x11.UserInfoResponse\x12,\n\x0bGetUserById\x12\n.IdRequest\x1a\x11.UserInfoResponse\x12\x30\n\nCreateUser\x12\x0f.CreateUserInfo\x1a\x11.UserInfoResponse\x12\x35\n\nUpdateUser\x12\x0f.UpdateUserInfo\x1a\x16.google.protobuf.EmptyB\x0cZ\nuser/protob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_PAGEINFO = _descriptor.Descriptor(
  name='PageInfo',
  full_name='PageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pn', full_name='PageInfo.pn', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pSize', full_name='PageInfo.pSize', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=80,
)


_MOBILEREQUEST = _descriptor.Descriptor(
  name='MobileRequest',
  full_name='MobileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobile', full_name='MobileRequest.mobile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=113,
)


_CREATEUSERINFO = _descriptor.Descriptor(
  name='CreateUserInfo',
  full_name='CreateUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickName', full_name='CreateUserInfo.nickName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passWord', full_name='CreateUserInfo.passWord', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='CreateUserInfo.mobile', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=183,
)


_UPDATEUSERINFO = _descriptor.Descriptor(
  name='UpdateUserInfo',
  full_name='UpdateUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UpdateUserInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='UpdateUserInfo.nickName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='UpdateUserInfo.gender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='birthDay', full_name='UpdateUserInfo.birthDay', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=265,
)


_IDREQUEST = _descriptor.Descriptor(
  name='IdRequest',
  full_name='IdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=278,
)


_USERINFORESPONSE = _descriptor.Descriptor(
  name='UserInfoResponse',
  full_name='UserInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserInfoResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passWord', full_name='UserInfoResponse.passWord', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='UserInfoResponse.mobile', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='UserInfoResponse.nickName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='birthDay', full_name='UserInfoResponse.birthDay', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='UserInfoResponse.gender', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='UserInfoResponse.role', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=411,
)


_USERLISTRESPONSE = _descriptor.Descriptor(
  name='UserListResponse',
  full_name='UserListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='UserListResponse.total', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='UserListResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=479,
)

_USERLISTRESPONSE.fields_by_name['data'].message_type = _USERINFORESPONSE
DESCRIPTOR.message_types_by_name['PageInfo'] = _PAGEINFO
DESCRIPTOR.message_types_by_name['MobileRequest'] = _MOBILEREQUEST
DESCRIPTOR.message_types_by_name['CreateUserInfo'] = _CREATEUSERINFO
DESCRIPTOR.message_types_by_name['UpdateUserInfo'] = _UPDATEUSERINFO
DESCRIPTOR.message_types_by_name['IdRequest'] = _IDREQUEST
DESCRIPTOR.message_types_by_name['UserInfoResponse'] = _USERINFORESPONSE
DESCRIPTOR.message_types_by_name['UserListResponse'] = _USERLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageInfo = _reflection.GeneratedProtocolMessageType('PageInfo', (_message.Message,), {
  'DESCRIPTOR' : _PAGEINFO,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:PageInfo)
  })
_sym_db.RegisterMessage(PageInfo)

MobileRequest = _reflection.GeneratedProtocolMessageType('MobileRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOBILEREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:MobileRequest)
  })
_sym_db.RegisterMessage(MobileRequest)

CreateUserInfo = _reflection.GeneratedProtocolMessageType('CreateUserInfo', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERINFO,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserInfo)
  })
_sym_db.RegisterMessage(CreateUserInfo)

UpdateUserInfo = _reflection.GeneratedProtocolMessageType('UpdateUserInfo', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERINFO,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUserInfo)
  })
_sym_db.RegisterMessage(UpdateUserInfo)

IdRequest = _reflection.GeneratedProtocolMessageType('IdRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDREQUEST,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:IdRequest)
  })
_sym_db.RegisterMessage(IdRequest)

UserInfoResponse = _reflection.GeneratedProtocolMessageType('UserInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERINFORESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserInfoResponse)
  })
_sym_db.RegisterMessage(UserInfoResponse)

UserListResponse = _reflection.GeneratedProtocolMessageType('UserListResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTRESPONSE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:UserListResponse)
  })
_sym_db.RegisterMessage(UserListResponse)


DESCRIPTOR._options = None

_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='User',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=482,
  serialized_end=738,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUserList',
    full_name='User.GetUserList',
    index=0,
    containing_service=None,
    input_type=_PAGEINFO,
    output_type=_USERLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserByMobile',
    full_name='User.GetUserByMobile',
    index=1,
    containing_service=None,
    input_type=_MOBILEREQUEST,
    output_type=_USERINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserById',
    full_name='User.GetUserById',
    index=2,
    containing_service=None,
    input_type=_IDREQUEST,
    output_type=_USERINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='User.CreateUser',
    index=3,
    containing_service=None,
    input_type=_CREATEUSERINFO,
    output_type=_USERINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUser',
    full_name='User.UpdateUser',
    index=4,
    containing_service=None,
    input_type=_UPDATEUSERINFO,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
