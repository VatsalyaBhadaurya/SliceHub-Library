from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

# dummy implementation for v0.1

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class JWTManager:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def create_token(self, data: dict) -> str:
        # TODO: implement JWT encoding
        return ""

    def verify_token(self, token: str) -> dict:
        # TODO: implement JWT decoding and verification
        return {}

    def get_current_user(self, token: str = Depends(oauth2_scheme)):
        # verify and return user info
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
