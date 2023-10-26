from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session  # type: ignore

from app import query
from app.db import SessionLocal
from app.model.cake import Cake
from app.schema.cake import CakeGet, CakeInsert

router = APIRouter(
    prefix="/cake",
    tags=["cake"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not Found"}},
)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.get("/", response_model=List[CakeGet])
async def get_all_cakes(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    cakes = query.get_cakes(session=session, skip=skip, limit=limit)
    return [i.serialize for i in cakes]


@router.get("/{cake_id}", response_model=CakeGet)
async def get_cake_by_id(cake_id: int, session: Session = Depends(get_session)):
    cake = query.get_cake_by_id(session=session, _id=cake_id)
    if cake is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cake not found"
        )
    return cake.serialize


@router.post("/", response_model=CakeGet, status_code=status.HTTP_201_CREATED)
async def add_cake(cake: CakeInsert, session: Session = Depends(get_session)):
    cake_db = query.get_cake_by_name(session=session, name=cake.name)
    if cake_db is not None:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Cake found")

    cake_db = Cake(
        _id=0,
        name=cake.name,
        comment=cake.comment,
        imageurl=cake.imageUrl,
        yumfactor=cake.yumFactor,
    )
    cake_inserted = query.add_cake(session=session, cake=cake_db)
    return cake_inserted.serialize


@router.delete("/{cake_id}")
async def delete_cake(cake_id: int, session: Session = Depends(get_session)):
    cake = query.get_cake_by_id(session=session, _id=cake_id)
    if cake is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cake not found"
        )

    _ = query.delete_cake(session=session, cake=cake)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
