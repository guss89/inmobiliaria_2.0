from fastapi import FastAPI
from app.database import engine, Base
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

from app.routers import empresa
from app.routers import etapa
from app.routers import lote
from app.routers import cliente

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500"
        ],  # Solo tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # O restringe a ["POST"] si solo usas POST
    allow_headers=["*"],  # O define encabezados específicos si prefieres
)

app.include_router(empresa.router)
app.include_router(etapa.router)
app.include_router(lote.router)
app.include_router(cliente.router)