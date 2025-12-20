from utils.TipoCombustivel import TipoCombustivel
from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
    id_posto: int
    data_hora: datetime
    tipo_combustivel: TipoCombustivel
    preco_por_litro: float
    volume_abastecido: float
    cpf_motorista: str
    improper_data: bool = False