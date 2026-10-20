import secrets
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

from db import get_key

key_scheme = APIKeyHeader(name = "x-key")


async def verify_key(x_key: Annotated[str, Depends(key_scheme)]):
    expected = get_key()
    if not secrets.compare_digest(expected, x_key):
        raise HTTPException(status_code=401, detail = "X-Key Invalid", headers = {"WWW-Authenticate": "ApiKey"})
