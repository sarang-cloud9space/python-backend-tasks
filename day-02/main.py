import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "products.json"

with open(DATA_FILE, "r", encoding="utf-8") as file:
    products = json.load(file)

print(products)

print(products[0])
print(products[0]["name"])
print(products[1]["price"])