from typing import Optional

from pydantic import BaseModel, validator


class CakeBase(BaseModel):
    name: str
    comment: str
    imageUrl: str
    yumFactor: int

    @validator("yumFactor")
    def check_range(cls, v):
        if v <= 0 or v > 5:
            raise ValueError("yumFactor must be between 1 and 5 inclusive")
        return v


class CakeDelete(BaseModel):
    id: int


class CakeInsert(CakeBase):
    pass


class CakeUpdate(BaseModel):
    id: int
    name: Optional[str]
    comment: Optional[str]
    imageUrl: Optional[str]
    yumFactor: Optional[int]

    @validator("yumFactor")
    def check_range(cls, v):
        if v <= 0 or v > 5:
            raise ValueError("yumFactor must be between 1 and 5 inclusive")
        return v


class CakeGet(CakeBase):
    id: int
