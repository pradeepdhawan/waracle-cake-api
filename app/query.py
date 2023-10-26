from typing import List

from sqlalchemy.orm import Session  # type: ignore

from .model.cake import Cake


def get_cake_by_id(session: Session, _id: int) -> Cake:
    return session.query(Cake).filter(Cake.id == _id).first()


def get_cake_by_name(session: Session, name: str) -> Cake:
    return session.query(Cake).filter(Cake.name == name).first()


def get_cakes(session: Session, skip: int = 0, limit: int = 100) -> List[Cake]:
    return session.query(Cake).offset(skip).limit(limit).all()


def add_cake(session: Session, cake: Cake):
    session.add(cake)
    session.commit()
    session.refresh(cake)
    return cake


def delete_cake(session: Session, cake: Cake) -> int:
    session.delete(cake)
    session.commit()
    return cake
