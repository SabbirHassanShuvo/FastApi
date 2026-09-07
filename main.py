from fastapi import FastAPI, Body

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

@app.post("/todos")
def create_todo(new_todo=Body()):
    Toods.append(new_todo)

    return {"message": "Todo created successfully", "todo": new_todo}

@app.put("/todos_update")
def update_todo(exiting_todo=Body()):
    Toods[0] = exiting_todo
    return {"message": "Todo updated successfully", "todo": exiting_todo}