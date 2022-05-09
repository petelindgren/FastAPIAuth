from fastapi_users.authentication.strategy import AccessTokenProtocol


class AccessToken(AccessTokenProtocol):
    class Config:
        orm_mode = True
