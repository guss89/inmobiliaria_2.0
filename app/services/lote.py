from sqlalchemy.orm import Session
from sqlalchemy import func, case, text
from typing import List, Dict

from app.schemas.lote import Lote

from app.models.lote import Lote


def get_all_lote(db:Session):
    return db.query(Lote).all()

