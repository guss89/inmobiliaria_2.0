from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models import Base, Contrato, Cliente


class Copropietario(Base):
    __tablename__ = "copropietarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contrato_id = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relaciones
    contrato = relationship("Contrato", backref="copropietarios")
    cliente = relationship("Cliente", backref="copropietarios")