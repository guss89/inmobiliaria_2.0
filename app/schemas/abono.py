from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import date, datetime

from app.schemas.usuario import UsuarioRead


class AbonoBase(BaseModel):
    recibo_id: int
    pago_planificado_id: Optional[int] = None
    monto_abono: condecimal(max_digits=12, decimal_places=2)
    fecha_abono: date
    user_id: int


class AbonoCreate(AbonoBase):
    pass


class AbonoUpdate(AbonoBase):
    pass


class Abono(AbonoBase):
    id: int
    usuario: UsuarioRead
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True 