import json

file_path = "src/utils/products.json"


def get_all_products():
    with open(file_path, 'r') as p:
        return json.load(p)