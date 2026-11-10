import pandas as pd
from Product import Product
from mongoDb import MongoDB

df = pd.read_excel("products.xlsx")

products = []

for _, row in df.iterrows():

    product = Product.from_dict(
        row.to_dict()
    )

    products.append(product)

db = MongoDB()

if db.kiem_tra_ket_noi():
    print("Ket noi MongoDB thanh cong")

data = [p.to_dict() for p in products]

db.collection.insert_many(data)

print("Import thanh cong")