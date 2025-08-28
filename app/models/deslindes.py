from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Date, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, Lote


class Deslinde(Base):
    __tablename__ = "deslindes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lote_id = Column(Integer, ForeignKey("lotes.id"), nullable=False)
    concepto = Column(String(150), nullable=False)
    monto = Column(DECIMAL(12, 2), nullable=False)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relación
    lote = relationship("Lote", backref="deslindes")
    usuario = relationship("Usuario", backref="deslindes")