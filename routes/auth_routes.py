from fastapi import APIRouter, HTTPException, Depends
from auth import verify_token
from models import User
from config import client, BQ_USERS_TABLE

router = APIRouter()

@router.post('/signup')
def register_user(user: User):
    query = f"""
    INSERT INTO `{BQ_USERS_TABLE}` (id, username, role)
    VALUES ('{user.id}', '{user.username}', '{user.role}')
    """
    client.query(query)
    return {"message": "User registered successfully"}

@router.get('/users/me')
def get_current_user(token: dict = Depends(verify_token)):
    user_id = token['uid']
    query = f"SELECT * FROM `{BQ_USERS_TABLE}` WHERE id = '{user_id}'"
    result = client.query(query).result()
    users = [dict(row) for row in result]
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[0]
