from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any
from enum import Enum


class EstatusLoteEnum(str, Enum):
    disponible = "disponible"
    apartado = "apartado"
    vendido = "vendido"
    litigio = "litigio"


class LoteBase(BaseModel):
    etapa_id: int
    numero: str
    superficie: Optional[float] = None
    colindancias: Optional[Dict[str, Any]] = None  # JSON en formato dict
    estatus: Optional[EstatusLoteEnum] = EstatusLoteEnum.disponible


class LoteCreate(LoteBase):
    pass


class LoteUpdate(LoteBase):
    pass


class Lote(LoteBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True  # antes orm_mode = True