from typing import List
from pydantic import BaseModel
from datetime import date


class Genre(BaseModel):
    name:str

class Author(BaseModel):
    fistName:str
    lastName:str
    age:int


class Book(BaseModel):
    title: str
    author: str
    genres: List[Genre] = None
    date: date
    pages: int



