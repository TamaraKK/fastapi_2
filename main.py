from fastapi import FastAPI, Request, Query
from schemas import Book
from typing import List

app = FastAPI()


@app.get('/home')
def home():
    return {'key':'Hello'}

@app.get('/{pk}')
def get_item(p: int, q:str = None):
    return {'key': p, 'q':q}


@app.post('/create_book')
def create_book(item: Book):
    return item

@app.get('/get_book')
def get_book(q:List[str] = Query(...,  description='search book')):
    return q








