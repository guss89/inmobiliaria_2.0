from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Date, Enum, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, PlanPago
import enum


class EstatusPagoPlanificadoEnum(str, enum.Enum):
    pendiente = "pendiente"
    pagado = "pagado"
    vencido = "vencido"


class PagoPlanificado(Base):
    __tablename__ = "pagos_planificados"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plan_id = Column(Integer, ForeignKey("planes_pago.id"), nullable=False)
    fecha_programada = Column(Date, nullable=False)
    monto_programado = Column(DECIMAL(12, 2), nullable=False)
    estatus = Column(Enum(EstatusPagoPlanificadoEnum), default=EstatusPagoPlanificadoEnum.pendiente)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relación
    plan = relationship("PlanPago", backref="pagos_planificados")