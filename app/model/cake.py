from typing import TypedDict

from sqlalchemy import CheckConstraint, Column, Integer, String  # type: ignore

from app.db import Base


class CakeDict(TypedDict):
    id: int
    name: str
    comment: str
    imageurl: str
    yumfactor: int


class Cake(Base):
    """
    Defines the cakes model
    """

    __tablename__ = "cake"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)
    comment = Column(String(200), nullable=False)
    imageurl = Column(String(255), nullable=False)
    yumfactor = Column(Integer, nullable=False)
    CheckConstraint("yumfactor>0 AND yumfactor<=5")

    def __init__(
        self, _id: int, name: str, comment: str, imageurl: str, yumfactor: int
    ):
        if _id != 0:
            _id = self.id
        self.name = name
        self.comment = comment
        self.imageurl = imageurl
        self.yumfactor = yumfactor

    def __repr__(self) -> str:
        return f"<Cake {self.name}>"

    @property
    def serialize(self) -> CakeDict:
        """
        Return cake in serializeable format
        """
        return {
            "id": self.id,
            "name": self.name,
            "comment": self.comment,
            "imageUrl": self.imageurl,
            "yumFactor": self.yumfactor,
        }
