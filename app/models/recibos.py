from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DECIMAL, Date, Text, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, Contrato, Cliente
import enum


class TipoCobroEnum(str, enum.Enum):
    efectivo = "efectivo"
    transferencia = "transferencia"
    tarjeta = "tarjeta"
    otro = "otro"


class Recibo(Base):
    __tablename__ = "recibos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    no_recibo = Column(String(50), nullable=False)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    fecha_cobro = Column(Date, nullable=False)
    monto_cobrado = Column(DECIMAL(12, 2), nullable=False)
    tipo_cobro = Column(Enum(TipoCobroEnum), default=TipoCobroEnum.efectivo)
    user_cobro = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    observaciones = Column(Text, nullable=True)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relaciones
    contrato = relationship("Contrato", backref="recibos")
    cliente = relationship("Cliente", backref="recibos")
    usuario = relationship("Usuario", backref="recibos")