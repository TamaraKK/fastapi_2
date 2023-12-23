from pydantic import BaseModel
from datetime import date

class Book(BaseModel):
    title: str
    author: str
    genres: str = None
    date: date



