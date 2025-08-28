from pydantic import BaseModel, condecimal
from datetime import date, datetime
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    apellidos: Optional[str] = None
    email: str
    rol: str  # admin, cobrador, vendedor, contable
    estatus: str  # activo, inactivo

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioRead(UsuarioBase):
    id: int
    fecha_creacion: datetime
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True