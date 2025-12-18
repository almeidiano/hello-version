from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JOSEError
from fastapi import Depends, HTTPException, status
from services.token import sign_jwt

class TipoCombustivel(str, Enum):
    'GASOLINA' == 'GASOLINA'
    'ETANOL' == 'ETANOL'
    'DIESEL' == 'DIESEL'

class Item(BaseModel):
    id_posto: int
    data_hora: datetime
    tipo_combustivel: TipoCombustivel
    preco_por_litro: float
    volume_abastecido: float
    cpf_motorista: str

app = FastAPI()

router = APIRouter(prefix="/api/v1")

@router.get("/token")
async def login():
    return sign_jwt()

security = HTTPBearer()

@router.post("/abastecimentos")
async def root(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    
    return {"message": "Conseguiu acessar.", "teu token": token}

app.include_router(router)