from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_date: Optional[date] = None
    rating: Optional[float] = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
