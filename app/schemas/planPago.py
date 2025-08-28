from pydantic import BaseModel, condecimal
from typing import Optional
from datetime import date, datetime
from enum import Enum


class EstatusPlanPagoEnum(str, Enum):
    vigente = "vigente"
    liquidado = "liquidado"
    cancelado = "cancelado"


class PlanPagoBase(BaseModel):
    contrato_id: int
    monto_total: condecimal(max_digits=12, decimal_places=2)
    no_pagos: int
    fecha_inicio: Optional[date] = None
    estatus: Optional[EstatusPlanPagoEnum] = EstatusPlanPagoEnum.vigente


class PlanPagoCreate(PlanPagoBase):
    pass


class PlanPagoUpdate(PlanPagoBase):
    pass


class PlanPago(PlanPagoBase):
    id: int
    updated_at: Optional[datetime]
    is_synced: int

    class Config:
        from_attributes = True 