from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class CopropietarioBase(BaseModel):
    contrato_id: int
    cliente_id: int


class CopropietarioCreate(CopropietarioBase):
    pass


class CopropietarioUpdate(CopropietarioBase):
    pass


class Copropietario(CopropietarioBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True  # antes orm_mode = True