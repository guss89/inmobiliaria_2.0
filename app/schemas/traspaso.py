from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import datetime

from app.schemas.usuario import UsuarioRead


class TraspasoBase(BaseModel):
    contrato_origen: int
    contrato_destino: int
    monto: condecimal(max_digits=12, decimal_places=2)
    user_autoriza: int


class TraspasoCreate(TraspasoBase):
    pass


class TraspasoUpdate(TraspasoBase):
    pass


class Traspaso(TraspasoBase):
    id: int
    usuario_autoriza: UsuarioRead
    fecha: datetime
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True  # antes orm_mode = True