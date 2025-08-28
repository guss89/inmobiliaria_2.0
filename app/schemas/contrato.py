from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import date, datetime
from enum import Enum

from app.schemas.usuario import UsuarioRead


class EstatusContratoEnum(str, Enum):
    activo = "activo"
    liquidado = "liquidado"
    rescindido = "rescindido"
    traspasado = "traspasado"


class ContratoBase(BaseModel):
    lote_id: int
    cliente_id: int
    fecha_contrato: date
    total: condecimal(max_digits=12, decimal_places=2)
    anticipo: Optional[condecimal(max_digits=12, decimal_places=2)] = 0
    total_pagos: Optional[int] = 0
    estatus: Optional[EstatusContratoEnum] = EstatusContratoEnum.activo
    user_id: int


class ContratoCreate(ContratoBase):
    pass


class ContratoUpdate(ContratoBase):
    pass


class Contrato(ContratoBase):
    id: int
    usuario: UsuarioRead
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True  # antes orm_mode = True