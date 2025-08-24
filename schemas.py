from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from enum import IntEnum

class EstadoRegistro(IntEnum):
    PENDIENTE = 1
    EN_REVISION = 2
    APROBADO = 3
    RECHAZADO = 4
    VIGENTE = 5
    VENCIDO = 6

# Esquema base para RegistroMarca
class RegistroMarcaBase(BaseModel):
    nombre_marca: str
    descripcion: Optional[str] = None
    categoria: str
    clase_niza: Optional[str] = None
    solicitante: str
    email_solicitante: EmailStr

# Esquema para crear un registro de marca
class RegistroMarcaCreate(RegistroMarcaBase):
    pass

# Esquema para actualizar un registro de marca
class RegistroMarcaUpdate(BaseModel):
    nombre_marca: Optional[str] = None
    descripcion: Optional[str] = None
    categoria: Optional[str] = None
    clase_niza: Optional[str] = None
    solicitante: Optional[str] = None
    email_solicitante: Optional[EmailStr] = None
    estado: Optional[EstadoRegistro] = None

# Esquema para la respuesta (lo que se devuelve al cliente)
class RegistroMarca(RegistroMarcaBase):
    id: int
    estado: EstadoRegistro
    numero_solicitud: Optional[str] = None
    fecha_solicitud: datetime
    fecha_aprobacion: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
