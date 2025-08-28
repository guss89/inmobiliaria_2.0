from sqlalchemy.orm import Session
from sqlalchemy import func, case, text
from typing import List, Dict

from app.schemas.empresas import Empresa

from app.models.empresa import Empresa

def get_all_empresa(db:Session):
    return db.query(Empresa).all()

