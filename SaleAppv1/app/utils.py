import json

def load_product():
    with open("data/products.json","r",encoding="utf-8") as f:
        products = json.load(f)
    return products