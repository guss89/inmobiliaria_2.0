from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import date, datetime
from enum import Enum


class EstatusPagoPlanificadoEnum(str, Enum):
    pendiente = "pendiente"
    pagado = "pagado"
    vencido = "vencido"


class PagoPlanificadoBase(BaseModel):
    plan_id: int
    fecha_programada: date
    monto_programado: condecimal(max_digits=12, decimal_places=2)
    estatus: Optional[EstatusPagoPlanificadoEnum] = EstatusPagoPlanificadoEnum.pendiente


class PagoPlanificadoCreate(PagoPlanificadoBase):
    pass


class PagoPlanificadoUpdate(PagoPlanificadoBase):
    pass


class PagoPlanificado(PagoPlanificadoBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True