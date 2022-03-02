# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"\x0e\n\x0cLoginRequest\"\x0f\n\rLoginResponse\"\x0f\n\rSignupRequest\"\x10\n\x0eSignupResponse\"\x0f\n\rLogoutRequest\"\x10\n\x0eLogoutResponse2\xa2\x01\n\x04\x41uth\x12\x30\n\x05login\x12\x12.auth.LoginRequest\x1a\x13.auth.LoginResponse\x12\x33\n\x06signup\x12\x13.auth.SignupRequest\x1a\x14.auth.SignupResponse\x12\x33\n\x06logout\x12\x13.auth.LogoutRequest\x1a\x14.auth.LogoutResponseb\x06proto3')



_LOGINREQUEST = DESCRIPTOR.message_types_by_name['LoginRequest']
_LOGINRESPONSE = DESCRIPTOR.message_types_by_name['LoginResponse']
_SIGNUPREQUEST = DESCRIPTOR.message_types_by_name['SignupRequest']
_SIGNUPRESPONSE = DESCRIPTOR.message_types_by_name['SignupResponse']
_LOGOUTREQUEST = DESCRIPTOR.message_types_by_name['LogoutRequest']
_LOGOUTRESPONSE = DESCRIPTOR.message_types_by_name['LogoutResponse']
LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.LoginResponse)
  })
_sym_db.RegisterMessage(LoginResponse)

SignupRequest = _reflection.GeneratedProtocolMessageType('SignupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.SignupRequest)
  })
_sym_db.RegisterMessage(SignupRequest)

SignupResponse = _reflection.GeneratedProtocolMessageType('SignupResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.SignupResponse)
  })
_sym_db.RegisterMessage(SignupResponse)

LogoutRequest = _reflection.GeneratedProtocolMessageType('LogoutRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTREQUEST,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.LogoutRequest)
  })
_sym_db.RegisterMessage(LogoutRequest)

LogoutResponse = _reflection.GeneratedProtocolMessageType('LogoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:auth.LogoutResponse)
  })
_sym_db.RegisterMessage(LogoutResponse)

_AUTH = DESCRIPTOR.services_by_name['Auth']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINREQUEST._serialized_start=20
  _LOGINREQUEST._serialized_end=34
  _LOGINRESPONSE._serialized_start=36
  _LOGINRESPONSE._serialized_end=51
  _SIGNUPREQUEST._serialized_start=53
  _SIGNUPREQUEST._serialized_end=68
  _SIGNUPRESPONSE._serialized_start=70
  _SIGNUPRESPONSE._serialized_end=86
  _LOGOUTREQUEST._serialized_start=88
  _LOGOUTREQUEST._serialized_end=103
  _LOGOUTRESPONSE._serialized_start=105
  _LOGOUTRESPONSE._serialized_end=121
  _AUTH._serialized_start=124
  _AUTH._serialized_end=286
# @@protoc_insertion_point(module_scope)