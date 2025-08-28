from typing import Optional
from pydantic import BaseModel, condecimal
from datetime import datetime

from app.schemas.usuario import UsuarioRead


class EgresoBase(BaseModel):
    empresa_id: int
    concepto: str
    monto: condecimal(max_digits=12, decimal_places=2)
    user_id: int


class EgresoCreate(EgresoBase):
    pass


class EgresoUpdate(EgresoBase):
    pass


class Egreso(EgresoBase):
    id: int
    usuario: UsuarioRead
    fecha: datetime
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True 