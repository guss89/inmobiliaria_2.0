from typing import Optional
from pydantic import BaseModel, condecimal
from datetime import date, datetime


class DeslindeBase(BaseModel):
    lote_id: int
    concepto: str
    monto: condecimal(max_digits=12, decimal_places=2)
    user_id: int
    fecha: date


class DeslindeCreate(DeslindeBase):
    pass


class DeslindeUpdate(DeslindeBase):
    pass


class Deslinde(DeslindeBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True 