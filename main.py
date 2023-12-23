from fastapi import FastAPI, Request
from schemas import Item
app = FastAPI()


@app.get('/home')
def home():
    return {'key':'Hello'}

@app.get('/{pk}')
def get_item(p: int, q:str = None):
    return {'key': p, 'q':q}

@app.post("/items/")
async def create_item(item: Item, request: Request):
    return {"item": item, "client_host": request.client.host}
