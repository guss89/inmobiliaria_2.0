from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DECIMAL, Date, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, Lote, Cliente
import enum


class EstatusContratoEnum(str, enum.Enum):
    activo = "activo"
    liquidado = "liquidado"
    rescindido = "rescindido"
    traspasado = "traspasado"


class Contrato(Base):
    __tablename__ = "contratos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lote_id = Column(Integer, ForeignKey("lotes.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    fecha_contrato = Column(Date, nullable=False)
    total = Column(DECIMAL(12, 2), nullable=False)
    anticipo = Column(DECIMAL(12, 2), default=0)
    total_pagos = Column(Integer, default=0)
    estatus = Column(Enum(EstatusContratoEnum), default=EstatusContratoEnum.activo)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relaciones
    lote = relationship("Lote", backref="contratos")
    cliente = relationship("Cliente", backref="contratos")
    usuario = relationship("Usuario", backref="contratos")