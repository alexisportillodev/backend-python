# CRUD de Registros de Marca - Prueba Técnica SignaIP

**Desarrollador**: Alexis Antonio Portillo Ortega 
**Fecha**: 24 agosto 2025  
**Empresa**: www.signaip.com

## 🌐 Acceso Público

**🔗 URL de la aplicación**: https://registro-marca-api.onrender.com  
**📚 Documentación de la API**: https://registro-marca-api.onrender.com/docs  
**❤️ Health Check**: https://registro-marca-api.onrender.com/health  

## 📋 Descripción del Proyecto

Sistema CRUD completo para la gestión de Registros de Marca, desarrollado como parte de la prueba técnica para el rol de Desarrollador FullStack en SignaIP.

### Funcionalidades Implementadas
- ✅ Crear registros de marca
- ✅ Listar todos los registros (con filtros por estado)
- ✅ Obtener registro específico por ID
- ✅ Buscar registro por número de solicitud
- ✅ Actualizar información de registros
- ✅ Eliminar registros
- ✅ Sistema de estados del registro
- ✅ Generación automática de números de solicitud
- ✅ Estadísticas básicas

## 🛠️ Tecnologías Utilizadas

### Backend
- **Framework**: FastAPI 0.104.1
- **Lenguaje**: Python 3.11
- **ORM**: SQLAlchemy 2.0.23
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Validación**: Pydantic 2.5.0 con email-validator
- **Servidor**: Uvicorn 0.24.0
- **Despliegue**: Render (gratuito)

### Librerías Principales
```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
python-dotenv==1.0.0
email-validator==2.1.0
```

## 🚀 API Endpoints

### Registros de Marca
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/registros/` | Crear nuevo registro de marca |
| `GET` | `/registros/` | Listar registros (con filtro por estado) |
| `GET` | `/registros/{id}` | Obtener registro específico |
| `GET` | `/registros/buscar/{numero}` | Buscar por número de solicitud |
| `PUT` | `/registros/{id}` | Actualizar registro |
| `DELETE` | `/registros/{id}` | Eliminar registro |

### Utilidades
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Información de la API |
| `GET` | `/health` | Estado del servicio |
| `GET` | `/estadisticas/` | Estadísticas del sistema |

## 📊 Modelo de Datos

### RegistroMarca
```json
{
  "id": 1,
  "nombre_marca": "TechBrand",
  "descripcion": "Marca de tecnología innovadora",
  "categoria": "Tecnología",
  "clase_niza": "09",
  "solicitante": "Juan Pérez",
  "email_solicitante": "juan@example.com",
  "estado": "pendiente",
  "numero_solicitud": "MR12345678",
  "fecha_solicitud": "2025-08-24T10:00:00Z",
  "fecha_aprobacion": null,
  "created_at": "2025-08-24T10:00:00Z",
  "updated_at": "2025-08-24T10:00:00Z"
}
```

### Estados Disponibles
- `pendiente`: Registro recién creado
- `en_revision`: En proceso de revisión
- `aprobado`: Aprobado para registro  
- `rechazado`: Solicitud rechazada
- `vigente`: Marca registrada y vigente
- `vencido`: Registro vencido

## 💻 Instalación y Uso Local

### Prerrequisitos
- Python 3.11+
- Git

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/registro-marca-crud.git
cd registro-marca-crud/backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
uvicorn main:app --reload
```

La aplicación estará disponible en: http://127.0.0.1:8000

## 🌐 Despliegue

**Plataforma**: Render (https://render.com)  
**Tipo**: Web Service gratuito  
**Base de datos**: SQLite (incluida en el despliegue)

### Configuración de Producción
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Health Check**: `/health`

## 📁 Estructura del Proyecto

```
crud-project/
├── backend-python/
│   ├── main.py           # Aplicación principal FastAPI
│   ├── database.py       # Configuración de base de datos
│   ├── models.py         # Modelos SQLAlchemy
│   ├── schemas.py        # Esquemas Pydantic
│   ├── crud.py          # Operaciones CRUD
│   ├── requirements.txt  # Dependencias Python
│   ├── render.yaml      # Configuración Render
│   ├── .gitignore       # Archivos ignorados por Git
│   └── README.md        # Documentación del backend
```

## 📝 Notas Técnicas

- **CORS**: Configurado para permitir peticiones desde cualquier origen
- **Documentación**: Swagger UI automática en `/docs`
- **Validación**: Esquemas Pydantic para validación de datos
- **Base de datos**: Migración automática de esquemas con SQLAlchemy
- **Números únicos**: Generación automática de números de solicitud
- **Timestamps**: Tracking automático de fechas de creación y actualización

## 🧪 Testing

Para probar la API, visita: https://registro-marca-api.onrender.com/docs

### Ejemplo de Creación
```json
POST /registros/
{
  "nombre_marca": "InnovaBrand",
  "descripcion": "Marca de productos innovadores",
  "categoria": "Tecnología",
  "clase_niza": "09",
  "solicitante": "María García",
  "email_solicitante": "maria@example.com"
}
```

---

**Desarrollado con ❤️ para SignaIP**
