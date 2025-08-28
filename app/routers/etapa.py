from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

from app.schemas.etapa import Etapa

from app.services.etapa import get_all_etapa

router =  APIRouter(prefix="/etapas", tags=["Etapas"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Etapa])
def list_all(db:Session = Depends(get_db)):
    return get_all_etapa(db)