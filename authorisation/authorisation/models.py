import resource


class Rescorce:
    
    resource_name: str
    resource_secret: bytes
    resource_id: int

class AuthGrant:

    grant: bytes
    rescource_id: str

class AccessToken:

    grants: list
    user_id: str