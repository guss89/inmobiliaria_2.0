from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class EstatusClienteEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"


class ClienteBase(BaseModel):
    nombre: str
    apellidos: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    estatus: Optional[EstatusClienteEnum] = EstatusClienteEnum.activo


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True  # antes orm_mode = True