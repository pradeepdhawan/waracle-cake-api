from typing import Optional

from pydantic import BaseModel, validator


class CakeBase(BaseModel):
    name: str
    comment: str
    imageUrl: str
    yumFactor: int

    @validator("name")
    def check_range(cls, v):
        if len(v) > 200:
            raise ValueError("Name can only be 30 characters long")
        return v

    @validator("comment")
    def check_range(cls, v):
        if len(v) > 200:
            raise ValueError("Comments can only be 200 characters long")
        return v

    @validator("yumFactor")
    def check_range(cls, v):
        if v <= 0 or v > 5:
            raise ValueError("yumFactor must be between 1 and 5 inclusive")
        return v


class CakeDelete(BaseModel):
    id: int


class CakeInsert(CakeBase):
    pass


class CakeGet(CakeBase):
    id: int
