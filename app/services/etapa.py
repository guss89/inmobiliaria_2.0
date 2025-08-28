from sqlalchemy.orm import Session
from sqlalchemy import func, case, text
from typing import List, Dict

from app.schemas.etapa import Etapa

from app.models.etapa import Etapa


def get_all_etapa(db:Session):
    return db.query(Etapa).all()

