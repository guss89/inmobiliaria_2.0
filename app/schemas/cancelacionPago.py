from pydantic import BaseModel, condecimal
from datetime import datetime
from typing import Optional

from app.schemas.usuario import UsuarioRead


class CancelacionPagoBase(BaseModel):
    plan_pagos_id: int
    monto: condecimal(max_digits=12, decimal_places=2)
    user_autoriza: int


class CancelacionPagoCreate(CancelacionPagoBase):
    pass


class CancelacionPagoUpdate(CancelacionPagoBase):
    pass


class CancelacionPago(CancelacionPagoBase):
    id: int
    usuario: UsuarioRead
    fecha: datetime
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True