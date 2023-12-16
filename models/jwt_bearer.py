from security.jwt_manager import token_validation
from models.user import user_admin

from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = token_validation(auth.credentials)
        if data["email"] != user_admin.email or data["password"] != user_admin.password:
            return HTTPException(status_code=401, detail="Unauthorized")