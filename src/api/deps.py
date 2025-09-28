"""
Defines dependencies used by the endpoints.
"""

from config import settings
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status

def api_key_auth(api_key: str = Depends(APIKeyHeader(name="Authorization"))):
    # Validate the provided API key
    if api_key != settings.API_KEY.get_secret_value():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
        )