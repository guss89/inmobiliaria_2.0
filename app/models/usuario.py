from enum import Enum
import enum
from sqlalchemy import TIMESTAMP, Column, Integer, String, func
from sqlalchemy.orm import relationship
from models import Base

class RolUsuarioEnum(str, enum.Enum):
    admin = "admin"
    cobrador = "cobrador"
    vendedor = "vendedor"
    contable = "contable"

class EstatusEmpresaEnum(str, enum.Enum):
    activo = "activo"
    inactivo = "inactivo"

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(150))
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    rol = Column(Enum(RolUsuarioEnum), default=RolUsuarioEnum.vendedor)
    estatus = Column(Enum(EstatusEmpresaEnum), default=EstatusEmpresaEnum.activo)
    fecha_creacion = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)