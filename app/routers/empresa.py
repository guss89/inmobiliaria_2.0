from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

from app.schemas.empresas import Empresa

from app.services.empresa import get_all_empresa

router =  APIRouter(prefix="/empresas", tags=["Empresas"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Empresa])
def list_all(db:Session = Depends(get_db)):
    return get_all_empresa(db)