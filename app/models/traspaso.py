from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, TIMESTAMP, func
from sqlalchemy.orm import relationship
from models import Base, Contrato


class Traspaso(Base):
    __tablename__ = "traspasos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contrato_origen = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    contrato_destino = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    monto = Column(DECIMAL(12, 2), nullable=False)
    user_autoriza = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_synced = Column(Integer, default=0)

    # Relaciones
    contrato_origen_rel = relationship("Contrato", foreign_keys=[contrato_origen], backref="traspasos_origen")
    contrato_destino_rel = relationship("Contrato", foreign_keys=[contrato_destino], backref="traspasos_destino")
    usuario_autoriza = relationship("Usuario", backref="traspasos_autorizados")