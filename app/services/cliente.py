from sqlalchemy.orm import Session
from sqlalchemy import func, case, text
from typing import List, Dict

from app.schemas.cliente import Cliente

from app.models.cliente import Cliente


def get_all_cliente(db:Session):
    return db.query(Cliente).all()
