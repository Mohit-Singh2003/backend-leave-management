from fastapi import APIRouter, HTTPException, Depends
from ..auth import verify_token
from ..models import User
from ..config import bigquery_client, BQ_USERS_TABLE
from ..utils.auth_utils import get_current_user
auth_router = APIRouter()

@auth_router.post('/signup')
async def register_user(user: User):
    query = f"""
    INSERT INTO `{BQ_USERS_TABLE}` (id, username, role)
    VALUES ('{user.id}', '{user.username}', '{user.role}') RETURNING *;
    """
    response = await bigquery_client.query(query)
    return {"message": "User registered successfully", user: response}

@auth_router.get('/users/me')
def get_current_users(token: dict = Depends(verify_token)):
    return get_current_user(token)


