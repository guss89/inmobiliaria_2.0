from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class EstatusEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"


class EtapaBase(BaseModel):
    empresa_id: int
    nombre: str
    paraje: Optional[str] = None
    direccion: Optional[str] = None
    jurisdiccion: Optional[str] = None
    estatus: Optional[EstatusEnum] = EstatusEnum.activo


class EtapaCreate(EtapaBase):
    pass


class EtapaUpdate(EtapaBase):
    pass


class Etapa(EtapaBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True  # antes orm_mode = True