from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")       # Base Path

def index():        # Path operation function
    return {"message": "Hello, World!"}

@app.get("/about")    # About Path
def about():
    return {"message": "This is the about page!"}


@app.get('/blog')                           # Sending data through query parameter
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')         # This path should be at top because fastapi matches the first path it finds.
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')                   # Sending data through path parameter
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


class Blog(BaseModel):                    # Blog is a class that inherits from BaseModel.
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):             # Here parameter blog is of type Blog, which is a Pydantic model.
    return {'data': f"Blog is created with title as {blog.title} and the desc is {blog.body} and published is {blog.published}"}