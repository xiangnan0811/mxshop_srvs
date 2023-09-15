from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PassWordCheckRequest(_message.Message):
    __slots__ = ["password", "encryptedPassword"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTEDPASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    encryptedPassword: str
    def __init__(self, password: _Optional[str] = ..., encryptedPassword: _Optional[str] = ...) -> None: ...

class PassWordCheckResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class PageInfo(_message.Message):
    __slots__ = ["pn", "pSize"]
    PN_FIELD_NUMBER: _ClassVar[int]
    PSIZE_FIELD_NUMBER: _ClassVar[int]
    pn: int
    pSize: int
    def __init__(self, pn: _Optional[int] = ..., pSize: _Optional[int] = ...) -> None: ...

class MobileRequest(_message.Message):
    __slots__ = ["mobile"]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    mobile: str
    def __init__(self, mobile: _Optional[str] = ...) -> None: ...

class CreateUserInfo(_message.Message):
    __slots__ = ["nickName", "passWord", "mobile"]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    nickName: str
    passWord: str
    mobile: str
    def __init__(self, nickName: _Optional[str] = ..., passWord: _Optional[str] = ..., mobile: _Optional[str] = ...) -> None: ...

class UpdateUserInfo(_message.Message):
    __slots__ = ["id", "nickName", "gender", "birthDay"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    nickName: str
    gender: str
    birthDay: int
    def __init__(self, id: _Optional[int] = ..., nickName: _Optional[str] = ..., gender: _Optional[str] = ..., birthDay: _Optional[int] = ...) -> None: ...

class IdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UserInfoResponse(_message.Message):
    __slots__ = ["id", "passWord", "mobile", "nickName", "birthDay", "gender", "role"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    passWord: str
    mobile: str
    nickName: str
    birthDay: int
    gender: str
    role: int
    def __init__(self, id: _Optional[int] = ..., passWord: _Optional[str] = ..., mobile: _Optional[str] = ..., nickName: _Optional[str] = ..., birthDay: _Optional[int] = ..., gender: _Optional[str] = ..., role: _Optional[int] = ...) -> None: ...

class UserListResponse(_message.Message):
    __slots__ = ["total", "data"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    total: int
    data: _containers.RepeatedCompositeFieldContainer[UserInfoResponse]
    def __init__(self, total: _Optional[int] = ..., data: _Optional[_Iterable[_Union[UserInfoResponse, _Mapping]]] = ...) -> None: ...
