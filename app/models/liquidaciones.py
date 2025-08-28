from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Date, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, Contrato


class Liquidacion(Base):
    __tablename__ = "liquidaciones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    monto_total = Column(DECIMAL(12, 2), nullable=False)
    monto_cobrado = Column(DECIMAL(12, 2), default=0)
    descuento = Column(DECIMAL(12, 2), default=0)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    autoriza_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relación
    contrato = relationship("Contrato", backref="liquidaciones")
    usuario = relationship("Usuario", foreign_keys=[user_id], backref="liquidaciones_realizadas")
    autoriza = relationship("Usuario", foreign_keys=[autoriza_id], backref="liquidaciones_autorizadas")