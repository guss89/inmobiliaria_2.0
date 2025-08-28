from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, TIMESTAMP, func
from sqlalchemy.orm import relationship
from models import Base, PlanPago


class CancelacionPago(Base):
    __tablename__ = "cancelacion_pagos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plan_pagos_id = Column(Integer, ForeignKey("planes_pago.id"), nullable=False)
    monto = Column(DECIMAL(12, 2), nullable=False)
    user_autoriza = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relación
    plan_pago = relationship("PlanPago", backref="cancelaciones")
    usuario = relationship("Usuario", backref="cancelaciones_autorizadas")