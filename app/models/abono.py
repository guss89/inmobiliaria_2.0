from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Date, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, Recibo, PagoPlanificado


class Abono(Base):
    __tablename__ = "abonos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    recibo_id = Column(Integer, ForeignKey("recibos.id"), nullable=False)
    pago_planificado_id = Column(Integer, ForeignKey("pagos_planificados.id"), nullable=True)
    monto_abono = Column(DECIMAL(12, 2), nullable=False)
    fecha_abono = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relaciones
    recibo = relationship("Recibo", backref="abonos")
    pago_planificado = relationship("PagoPlanificado", backref="abonos")
    usuario = relationship("Usuario", backref="abonos")