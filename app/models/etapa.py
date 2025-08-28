from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.database import Base


class EstatusEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"


class Etapa(Base):
    __tablename__ = "etapas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    nombre = Column(String(100), nullable=False)
    paraje = Column(String(100), nullable=True)
    direccion = Column(String(200), nullable=True)
    jurisdiccion = Column(String(100), nullable=True)
    estatus = Column(Enum(EstatusEnum), default=EstatusEnum.activo)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relación con empresa
    empresa = relationship("Empresa", backref="etapas")