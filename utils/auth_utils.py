from fastapi import HTTPException, Header
from firebase_admin import auth as firebase_auth

def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        decoded_token = firebase_auth.verify_id_token(token)
        return decoded_token
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
