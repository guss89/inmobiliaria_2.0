from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base
import enum


class EstatusClienteEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(150), nullable=True)
    telefono = Column(String(20), nullable=True)
    direccion = Column(String(200), nullable=True)
    estatus = Column(Enum(EstatusClienteEnum), default=EstatusClienteEnum.activo)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)