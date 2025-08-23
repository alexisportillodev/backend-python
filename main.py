from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional

import models
import schemas
import crud
from database import SessionLocal, engine, get_db

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Registros de Marca",
    description="Sistema CRUD para gestión de registros de marca",
    version="1.0.0"
)

# Configurar CORS para permitir peticiones del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta básica
@app.get("/")
def read_root():
    return {
        "message": "API de Registros de Marca",
        "version": "1.0.0",
        "endpoints": "/docs"
    }

# Ruta de salud
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "registro-marca-api"}

# Crear registro de marca
@app.post("/registros/", response_model=schemas.RegistroMarca)
def create_registro(registro: schemas.RegistroMarcaCreate, db: Session = Depends(get_db)):
    return crud.create_registro_marca(db=db, registro=registro)

# Obtener todos los registros de marca
@app.get("/registros/", response_model=List[schemas.RegistroMarca])
def read_registros(
    skip: int = 0, 
    limit: int = 100,
    estado: Optional[schemas.EstadoRegistro] = Query(None, description="Filtrar por estado"),
    db: Session = Depends(get_db)
):
    if estado:
        registros = crud.get_registros_by_estado(db, estado=estado, skip=skip, limit=limit)
    else:
        registros = crud.get_registros_marca(db, skip=skip, limit=limit)
    return registros

# Obtener registro por ID
@app.get("/registros/{registro_id}", response_model=schemas.RegistroMarca)
def read_registro(registro_id: int, db: Session = Depends(get_db)):
    db_registro = crud.get_registro_marca(db, registro_id=registro_id)
    if db_registro is None:
        raise HTTPException(status_code=404, detail="Registro de marca no encontrado")
    return db_registro

# Buscar registro por número de solicitud
@app.get("/registros/buscar/{numero_solicitud}", response_model=schemas.RegistroMarca)
def buscar_registro_por_numero(numero_solicitud: str, db: Session = Depends(get_db)):
    db_registro = crud.get_registro_by_numero(db, numero_solicitud=numero_solicitud)
    if db_registro is None:
        raise HTTPException(status_code=404, detail="Número de solicitud no encontrado")
    return db_registro

# Actualizar registro de marca
@app.put("/registros/{registro_id}", response_model=schemas.RegistroMarca)
def update_registro(registro_id: int, registro: schemas.RegistroMarcaUpdate, db: Session = Depends(get_db)):
    db_registro = crud.update_registro_marca(db, registro_id=registro_id, registro=registro)
    if db_registro is None:
        raise HTTPException(status_code=404, detail="Registro de marca no encontrado")
    return db_registro

# Eliminar registro de marca
@app.delete("/registros/{registro_id}", response_model=schemas.RegistroMarca)
def delete_registro(registro_id: int, db: Session = Depends(get_db)):
    db_registro = crud.delete_registro_marca(db, registro_id=registro_id)
    if db_registro is None:
        raise HTTPException(status_code=404, detail="Registro de marca no encontrado")
    return db_registro

# Obtener estadísticas básicas
@app.get("/estadisticas/")
def get_estadisticas(db: Session = Depends(get_db)):
    total_registros = db.query(models.RegistroMarca).count()
    registros_por_estado = {}
    
    for estado in schemas.EstadoRegistro:
        count = db.query(models.RegistroMarca).filter(models.RegistroMarca.estado == estado).count()
        registros_por_estado[estado.value] = count
    
    return {
        "total_registros": total_registros,
        "registros_por_estado": registros_por_estado
    }
