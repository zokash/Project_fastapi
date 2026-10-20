from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import APIKeyHeader

key_scheme = APIKeyHeader(name = "x-key")
token_scheme = APIKeyHeader(name = "x-token")

async def verify_token(x_token: Annotated[str, Depends(token_scheme)]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=401, detail="X-Token header invalid")


async def verify_key(x_key:  Annotated[str,Depends(key_scheme)]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=401, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]