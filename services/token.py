import time
from fastapi.security import HTTPBearer
from jose import jwt

security = HTTPBearer()
JWT_SECRET="ASLDKJALÇSDKÇASJKASJD"
JWT_ALGORITHM="HS256"

def sign_jwt_token() -> dict:
    payload = {
        "sub": "vlab",
        "iat": time.time(),
        "exp": time.time() + 3600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}
