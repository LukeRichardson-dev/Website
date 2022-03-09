from calendar import timegm
from datetime import datetime, timezone, timedelta
from .auth_pb2 import LoginRequest, LoginResponse, RefreshRequest, RefreshResposne, SignupRequest, SignupResponse
from .auth_pb2_grpc import AuthServicer
from sqlalchemy.orm import Session, Query
from .base import NewSession
from .models import Account, Token
import random
from hashlib import sha256
from cryptography.hazmat.primitives import serialization
import jwt
from os import environ

class AuthService(AuthServicer):

    def __init__(self):
        self.session: Session = NewSession()

        key_dir = environ.get('KEY_DIR', '.ssh/')

        with open(f'{key_dir}auth_keys', 'rb') as f:

            private_key = f.read()
        
        self.private_key = serialization.load_ssh_private_key(private_key, password=b'')

        with open(f'{key_dir}auth_keys.pub', 'rb') as f:

            public_key = f.read()
        
        self.public_key = serialization.load_ssh_public_key(public_key)

    def signup(self, request: SignupRequest, context):
        assert request.HasField('username')
        assert request.HasField('password')

        base: Query = self.session.query(Account)

        user_exists_query: Query[Account] = base.filter(Account.username == request.username).limit(1)
        
        users = user_exists_query.all()
        assert not users

        secret = self.create_secret()
        salted_password = self.salt_password(request.password, secret)

        account = Account()

        account.username = request.username,
        account.password = salted_password,
        account.salt = secret,

        self.session.add(account)
        self.session.commit()

        added_account_result = base.filter(Account.username == request.username) \
                        .limit(1).all()

        assert added_account_result
        added_account: Account = added_account_result[0]

        refresh_token = self.create_refresh_token(
            added_account.account_id
        )

        self.upload_token(refresh_token, added_account)
        
        return SignupResponse(
            refreshToken=refresh_token
        )

    @staticmethod
    def create_secret():
        return random.randbytes(64)

    @staticmethod
    def salt_password(password, salt):
        hashed_password = sha256()
        hashed_password.update(password.encode())
        hashed_password.update(salt)
        return hashed_password.digest()

    def create_refresh_token(self, user_id):
        payload_data = {
            'type': 'refresh',
            'exp': timegm((datetime.now(tz=timezone.utc) + timedelta(days=30)).utctimetuple()),
            'user_id': user_id,
        }

        return self.sign_jwt(payload_data)

    def create_access_token(self, user_id, username):
        payload_data = {
            'type': 'access',
            'exp': timegm((datetime.now(tz=timezone.utc) + timedelta(minutes=15)).utctimetuple()),
            'user_id': user_id,
            'username': username,
        }

        return self.sign_jwt(payload_data)

    def sign_jwt(self, payload):
        token = jwt.encode(
            payload,
            algorithm="RS256",
            key=self.private_key,
        )

        return token.encode()

    def upload_token(self, token, account):
    
        token = Token()

        token.token = token
        token.owner = account

        self.session.add(token)

        self.session.commit()

    def login(self, request: LoginRequest, context):
        assert request.HasField('username')
        assert request.HasField('password')

        users = self.session.query(Account).filter(Account.username == request.username).limit(1).all()
        assert users
        user: Account = users[0]

        salted_password = self.salt_password(request.password, user.salt)
        assert salted_password == user.password

        token = self.create_refresh_token(user.account_id)
        self.upload_token(token, user)

        return LoginResponse(
            refreshToken=token,
        )

    def logout(self, request, context):
        return super().logout(request, context)

    def verify_token(self, token: bytes, type):

        decoded = jwt.decode(
            token.decode(),
            algorithms="RS256",
            key=self.public_key,
            leeway=timedelta(days=1),
        )

        user: Account = self.get_account_and_tokens(decoded['user_id'], token)
        assert user.tokens

        return user
        
    def get_account_and_tokens(self, id, token):

        users: Query[Account, Token] = self.session.query(Account) \
                    .join(Account.tokens, Token.token == token) \
                    .filter(Account.id == id) \
                    .limit(1).all()

        assert users

        return users[0]
        

    def refresh(self, request: RefreshRequest, context):
        user: Account = self.verify_token(request.refreshToken)

        token = self.create_access_token(user.account_id, user.username)

        return RefreshResposne(
            accessToken=token,
        )