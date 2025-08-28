from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import date, datetime
from enum import Enum

from app.schemas.usuario import UsuarioRead


class TipoCobroEnum(str, Enum):
    efectivo = "efectivo"
    transferencia = "transferencia"
    tarjeta = "tarjeta"
    otro = "otro"


class ReciboBase(BaseModel):
    no_recibo: str
    contrato_id: int
    cliente_id: int
    fecha_cobro: date
    monto_cobrado: condecimal(max_digits=12, decimal_places=2)
    tipo_cobro: Optional[TipoCobroEnum] = TipoCobroEnum.efectivo
    user_cobro: int
    observaciones: Optional[str] = None


class ReciboCreate(ReciboBase):
    pass


class ReciboUpdate(ReciboBase):
    pass


class Recibo(ReciboBase):
    id: int
    usuario: UsuarioRead
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True 