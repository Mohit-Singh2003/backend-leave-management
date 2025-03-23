from fastapi import HTTPException, Header
from firebase_admin import auth as firebase_auth
from fastapi import HTTPException
from ..config import bigquery_client, BQ_USERS_TABLE



def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        decoded_token = firebase_auth.verify_id_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
def get_user_role(token: dict):
    return token.get('role', 'employee')

def get_current_user(token):
    user_id = token['uid']
    query = f"SELECT * FROM `{BQ_USERS_TABLE}` WHERE id = '{user_id}'"
    result = bigquery_client.query(query).result()
    users = [dict(row) for row in result]
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[0]