import json
import csv
import os
#opening a json file


script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "products.json")
csv_path = os.path.join(script_dir, "filtered_products.csv")

try:
    with open(json_path, "r") as f:
        products = json.load(f)
except FileNotFoundError:
    print("Error: products.json not found. Check the file exists in this folder.")
    exit()
except json.JSONDecodeError:
    print("Error: prodcuts.json is not valid JSON. Check for missing commas or brackets.")
    exit()

#printing for sanity checking
# print(products)

#data filtering

    filtered_products = [
        p for p in products
        if p["in_stock"] and p["price"] > 50

    ]

    print(filtered_products)

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "category", "in_stock"])
        writer.writeheader()
        writer.writerows(filtered_products)
