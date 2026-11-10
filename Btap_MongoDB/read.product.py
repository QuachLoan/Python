#4. Chuyển DataFrame thành Object
import pandas as pd
from Product import Product

df = pd.read_excel("products.xlsx")

products = []

for _, row in df.iterrows():

    p = Product.from_dict(
        row.to_dict()
    )

    products.append(p)
# Hiển thị danh sách sản phẩm
for p in products:
    print(p)
print(
    "Tong so san pham:",
    len(products)
)