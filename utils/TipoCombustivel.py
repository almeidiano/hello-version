from enum import Enum

class TipoCombustivel(str, Enum):
    GASOLINA = 'GASOLINA'
    ETANOL = 'ETANOL'
    DIESEL = 'DIESEL'
    
class PrecoCombustivel(float, Enum):
    GASOLINA = 5.77
    ETANOL = 4.16
    DIESEL = 6.07