from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")       # Base Path

def index():        # Path operation function
    return {"message": "Hello, World!"}

@app.get("/about")    # About Path
def about():
    return {"message": "This is the about page!"}


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')         # This path should be at top because fastapi matches the first path it finds.
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}