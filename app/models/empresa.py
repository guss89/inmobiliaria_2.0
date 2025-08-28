from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import enum

Base = declarative_base()

class EstatusEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    estatus = Column(Enum(EstatusEnum), default=EstatusEnum.activo)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)