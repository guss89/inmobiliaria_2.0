from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class EstatusEnum(str, Enum):
    activo = "activo"
    inactivo = "inactivo"

class EmpresaBase(BaseModel):
    nombre: str
    estatus: Optional[EstatusEnum] = EstatusEnum.activo

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True  # antes orm_mode = True