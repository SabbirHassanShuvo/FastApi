from fastapi import APIRouter
from src.utils.utils import get_all_products

product_router = APIRouter()

@product_router.get("/")
def get_all_products():
    return get_all_products()

@product_router.post("/create")
def create_product():
    return {"message": "Product created successfully"}