from fastapi import FastAPI, Request
from schemas import Book

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
