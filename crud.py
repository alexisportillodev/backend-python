from sqlalchemy.orm import Session
from models import RegistroMarca, EstadoRegistro
from schemas import RegistroMarcaCreate, RegistroMarcaUpdate
import random
import string

def generar_numero_solicitud():
    """Genera un número único de solicitud"""
    return "MR" + "".join(random.choices(string.digits, k=8))

# Crear registro de marca
def create_registro_marca(db: Session, registro: RegistroMarcaCreate):
    numero_solicitud = generar_numero_solicitud()
    
    # Verificar que el número sea único
    while db.query(RegistroMarca).filter(RegistroMarca.numero_solicitud == numero_solicitud).first():
        numero_solicitud = generar_numero_solicitud()
    
    db_registro = RegistroMarca(
        nombre_marca=registro.nombre_marca,
        descripcion=registro.descripcion,
        categoria=registro.categoria,
        clase_niza=registro.clase_niza,
        solicitante=registro.solicitante,
        email_solicitante=registro.email_solicitante,
        numero_solicitud=numero_solicitud,
        estado=EstadoRegistro.PENDIENTE
    )
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

# Obtener registro por ID
def get_registro_marca(db: Session, registro_id: int):
    return db.query(RegistroMarca).filter(RegistroMarca.id == registro_id).first()

# Obtener registro por número de solicitud
def get_registro_by_numero(db: Session, numero_solicitud: str):
    return db.query(RegistroMarca).filter(RegistroMarca.numero_solicitud == numero_solicitud).first()

# Obtener todos los registros
def get_registros_marca(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RegistroMarca).offset(skip).limit(limit).all()

# Obtener registros por estado
def get_registros_by_estado(db: Session, estado: EstadoRegistro, skip: int = 0, limit: int = 100):
    return db.query(RegistroMarca).filter(RegistroMarca.estado == estado).offset(skip).limit(limit).all()

# Actualizar registro
def update_registro_marca(db: Session, registro_id: int, registro: RegistroMarcaUpdate):
    db_registro = db.query(RegistroMarca).filter(RegistroMarca.id == registro_id).first()
    if db_registro:
        update_data = registro.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_registro, field, value)
        db.commit()
        db.refresh(db_registro)
    return db_registro

# Eliminar registro
def delete_registro_marca(db: Session, registro_id: int):
    db_registro = db.query(RegistroMarca).filter(RegistroMarca.id == registro_id).first()
    if db_registro:
        db.delete(db_registro)
        db.commit()
    return db_registro