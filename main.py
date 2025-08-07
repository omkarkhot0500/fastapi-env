from fastapi import FastAPI

app = FastAPI()

@app.get("/")       # Base Path

def index():        # Path operation function
    return {"message": "Hello, World!"}

@app.get("/about")    # About Path
def about():
    return {"message": "This is the about page!"}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}