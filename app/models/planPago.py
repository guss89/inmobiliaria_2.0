from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Date, Enum, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, Contrato
import enum


class EstatusPlanPagoEnum(str, enum.Enum):
    vigente = "vigente"
    liquidado = "liquidado"
    cancelado = "cancelado"


class PlanPago(Base):
    __tablename__ = "planes_pago"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    monto_total = Column(DECIMAL(12, 2), nullable=False)
    no_pagos = Column(Integer, nullable=False)
    fecha_inicio = Column(Date, nullable=True)
    estatus = Column(Enum(EstatusPlanPagoEnum), default=EstatusPlanPagoEnum.vigente)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relación con contrato
    contrato = relationship("Contrato", backref="planes_pago")