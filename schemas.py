from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name:str

class Author(BaseModel):
    fistName:str = Field(..., max_length=25)
    lastName:str
    age:int = Field(..., gt=15, lt=100, description='author sge must be more than 15 and less than 100')

    # @validator('age')
    # def check_age(cls, v):
    #     if v<15: 
    #         raise ValueError('author sge must be more than 15')
    #     return v

class Book(BaseModel):
    title: str
    author: str
    genres: List[Genre] = []
    date: date
    pages: int


class BookOut(Book):
    id:int 

