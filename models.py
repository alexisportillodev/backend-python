from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from sqlalchemy.sql import func
from database import Base
import enum

class EstadoRegistro(enum.Enum):
    PENDIENTE = "pendiente"
    EN_REVISION = "en_revision"
    APROBADO = "aprobado"
    RECHAZADO = "rechazado"
    VIGENTE = "vigente"
    VENCIDO = "vencido"

class RegistroMarca(Base):
    __tablename__ = "registros_marca"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_marca = Column(String(255), nullable=False, index=True)
    descripcion = Column(Text, nullable=True)
    categoria = Column(String(100), nullable=False)
    clase_niza = Column(String(10), nullable=True)  # Clasificación internacional de Niza
    solicitante = Column(String(255), nullable=False)
    email_solicitante = Column(String(255), nullable=False)
    estado = Column(Enum(EstadoRegistro), default=EstadoRegistro.PENDIENTE)
    numero_solicitud = Column(String(50), unique=True, nullable=True)
    fecha_solicitud = Column(DateTime(timezone=True), server_default=func.now())
    fecha_aprobacion = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

