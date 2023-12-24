from fastapi import FastAPI, Request, Query, Path, Body, UploadFile, File
from schemas import Book, Author, BookOut
from typing import List
import shutil

app = FastAPI()



@app.post('/upload_file')
async def upload_file(file:UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {'file_name': file.filename}


@app.post('/upload_img')
async def upload_img(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {'file_name': 'good'}



@app.get('/home')
def home():
    return {'key':'Hello'}

@app.get('/{p}')
def get_item(p: int, q:str = None):
    return {'key': p, 'q':q}

@app.post('/create_author')
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}

# @app.post('/create_book')
# def create_book(item: Book, author: Author, quantity: int = Body(...)):
#     return {'item': item, 'author': author, 'quantity': quantity}

@app.post('/create_book', response_model=BookOut)
def create_book(item:Book):
    return BookOut(**item.dict(), id=3)

# ,response_model_exclude_unset=True, response_model_exclude={'pages', 'date'}

@app.get('/get_book')
def get_book(q:List[str] = Query(...,  description='search book')):
    return q

@app.get('/get_single_book/{id}')
def get_single_book(id:int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {'id': id, 'pages': pages}






