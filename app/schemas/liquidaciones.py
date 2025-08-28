from pydantic import BaseModel, condecimal
from datetime import date, datetime
from typing import Optional

from app.schemas.usuario import UsuarioRead


class LiquidacionBase(BaseModel):
    contrato_id: int
    monto_total: condecimal(max_digits=12, decimal_places=2)
    monto_cobrado: Optional[condecimal(max_digits=12, decimal_places=2)] = 0
    descuento: Optional[condecimal(max_digits=12, decimal_places=2)] = 0
    user_id: int
    autoriza_id: int
    fecha: date


class LiquidacionCreate(LiquidacionBase):
    pass


class LiquidacionUpdate(LiquidacionBase):
    pass


class Liquidacion(LiquidacionBase):
    id: int
    usuario: UsuarioRead
    autoriza: UsuarioRead
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True 