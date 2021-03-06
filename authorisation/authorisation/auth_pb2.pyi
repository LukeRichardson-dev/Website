"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AuthError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    code: typing.Text
    message: typing.Text
    def __init__(self,
        *,
        code: typing.Text = ...,
        message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code",b"code","message",b"message"]) -> None: ...
global___AuthError = AuthError

class LoginRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    username: typing.Text
    password: typing.Text
    def __init__(self,
        *,
        username: typing.Text = ...,
        password: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password",b"password","username",b"username"]) -> None: ...
global___LoginRequest = LoginRequest

class LoginResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFRESHTOKEN_FIELD_NUMBER: builtins.int
    EXPIRY_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    refreshToken: builtins.bytes
    expiry: typing.Text
    @property
    def error(self) -> global___AuthError: ...
    def __init__(self,
        *,
        refreshToken: builtins.bytes = ...,
        expiry: typing.Text = ...,
        error: typing.Optional[global___AuthError] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","expiry",b"expiry","refreshToken",b"refreshToken"]) -> None: ...
global___LoginResponse = LoginResponse

class SignupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    USERNAME_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    username: typing.Text
    password: typing.Text
    def __init__(self,
        *,
        username: typing.Text = ...,
        password: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["password",b"password","username",b"username"]) -> None: ...
global___SignupRequest = SignupRequest

class SignupResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFRESHTOKEN_FIELD_NUMBER: builtins.int
    EXPIRY_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    refreshToken: builtins.bytes
    expiry: typing.Text
    @property
    def error(self) -> global___AuthError: ...
    def __init__(self,
        *,
        refreshToken: builtins.bytes = ...,
        expiry: typing.Text = ...,
        error: typing.Optional[global___AuthError] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","expiry",b"expiry","refreshToken",b"refreshToken"]) -> None: ...
global___SignupResponse = SignupResponse

class LogoutRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFRESHTOKEN_FIELD_NUMBER: builtins.int
    refreshToken: builtins.bytes
    def __init__(self,
        *,
        refreshToken: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["refreshToken",b"refreshToken"]) -> None: ...
global___LogoutRequest = LogoutRequest

class LogoutResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___LogoutResponse = LogoutResponse

class RefreshRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFRESHTOKEN_FIELD_NUMBER: builtins.int
    refreshToken: builtins.bytes
    def __init__(self,
        *,
        refreshToken: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["refreshToken",b"refreshToken"]) -> None: ...
global___RefreshRequest = RefreshRequest

class RefreshResposne(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCESSTOKEN_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    accessToken: builtins.bytes
    @property
    def error(self) -> global___AuthError: ...
    def __init__(self,
        *,
        accessToken: builtins.bytes = ...,
        error: typing.Optional[global___AuthError] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accessToken",b"accessToken","error",b"error"]) -> None: ...
global___RefreshResposne = RefreshResposne
