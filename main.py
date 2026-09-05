from fastapi import FastAPI

app = FastAPI()

Toods =[
    {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
    {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
    {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
    {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
    {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
    {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False}
]

@app.get("/")
def heello_world():
    return {"message": "Hello, World!"}


@app.get("/todos")
def get_todos():
    return Toods