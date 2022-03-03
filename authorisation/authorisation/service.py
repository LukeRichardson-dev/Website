from .auth_pb2 import LoginRequest
from auth_pb2_grpc import AuthServicer

class AuthService(AuthServicer):

    def signup(self, request, context):
        return super().signup(request, context)

    def login(self, request, context):
        return super().login(request, context)

    def logout(self, request, context):
        return super().logout(request, context)