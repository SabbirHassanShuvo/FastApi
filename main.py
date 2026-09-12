from fastapi import FastAPI, Body
# Routes
from src.routes.productRoute import product_router

app = FastAPI()

# Toods =[
#     {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
#     {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
#     {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
#     {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
#     {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
#     {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
#     {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False}
# ]

# @app.get("/")
# def heello_world():
#     return {"message": "Hello, World!"}


# @app.get("/todos")
# def get_todos():
#     return Toods

# @app.post("/todos")
# def create_todo(new_todo=Body()):
#     Toods.append(new_todo)

#     return {"message": "Todo created successfully", "todo": new_todo}

# @app.put("/todos_update")
# def update_todo(exiting_todo=Body()):
#     Toods[0] = exiting_todo
#     return {"message": "Todo updated successfully", "todo": exiting_todo}


# ===== working with products =====

# @app.get("/products")
# def get_products():
#     return products

# # path param
# @app.get("/products/{product_id}")
# def get_one_product(product_id: int):

#     for one_product in products:
#         if one_product.get("id") == product_id:
#             return one_product

#     return{"message": "Product not found"}


# Crud operations json file
app.include_router(product_router, prefix="/products")
