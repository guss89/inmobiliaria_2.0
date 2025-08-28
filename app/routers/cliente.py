from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, database, services

from app.schemas.cliente import Cliente

from app.services.cliente import get_all_cliente

router =  APIRouter(prefix="/clientes", tags=["Clientes"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Cliente])
def list_all(db:Session = Depends(get_db)):
    return get_all_cliente(db)