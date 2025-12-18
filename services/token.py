import time
from datetime import datetime
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JOSEError
from fastapi import Depends, HTTPException, status

security = HTTPBearer()
JWT_SECRET="ASLDKJALÇSDKÇASJKASJD"
JWT_ALGORITHM="HS256"

def sign_jwt() -> dict:
    payload = {
        "sub": "vlab",
        "iat": time.time(),
        "exp": time.time() + 3600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

# def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     token = credentials.credentials
#     try:
#         # Decode and verify the JWT (add 'algorithms' parameter in a real app)
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         # You can add further checks here (e.g., expiration, user scopes)
#         return payload
#     except JOSEError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
