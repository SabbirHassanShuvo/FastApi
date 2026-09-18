import json
from pathlib import Path
from fastapi import FastAPI, Body

app = FastAPI()

# -------------------------------------------------------------
# প্রজেক্ট ডিরেক্টরি থেকে ডাটা ফাইল লোড করার সহজ নিয়ম:
# Path(__file__).resolve().parent দিলে main.py যে ফোল্ডারে আছে সেই পাথ নিশ্চিত করে
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
PRODUCTS_FILE = BASE_DIR / "src" / "data" / "products.json"

# JSON ফাইলটি ওপেন করে পাইথন লিস্টে লোড করা হচ্ছে
with open(PRODUCTS_FILE, "r", encoding="utf-8") as file:
    products = json.load(file)

Toods =[
    {"title": "Learn FastAPI", "description": "Learn how to build APIs with FastAPI", "done": False},
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


# ===== working with products =====

@app.get("/products")
def get_products():
    return products

# path param
@app.get("/products/{product_id}")
def get_one_product(product_id: int):

    for one_product in products:
        if one_product.get("id") == product_id:
            return one_product

    return{"message": "Product not found"}



