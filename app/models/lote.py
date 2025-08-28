from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DECIMAL, JSON, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.database import Base

class EstatusLoteEnum(str, enum.Enum):
    disponible = "disponible"
    apartado = "apartado"
    vendido = "vendido"
    litigio = "litigio"


class Lote(Base):
    __tablename__ = "lotes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    etapa_id = Column(Integer, ForeignKey("etapas.id"), nullable=False)
    numero = Column(String(50), nullable=False)
    superficie = Column(DECIMAL(10, 2), nullable=True)
    colindancias = Column(JSON, nullable=True)
    estatus = Column(Enum(EstatusLoteEnum), default=EstatusLoteEnum.disponible)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relación con etapa
    etapa = relationship("Etapa", backref="lotes")