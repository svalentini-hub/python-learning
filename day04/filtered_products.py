import json
import csv

#opening a json file
with open("products.json", "r") as f:
    products = json.load(f)

#printing for sanity checking
# print(products)

#data filtering

filtered_products = [
    p for p in products
    if p["in_stock"] and p["price"] > 50

]

print(filtered_products)

with open("filtered_products.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "price", "category", "in_stock"])
    writer.writeheader()
    writer.writerows(filtered_products)
