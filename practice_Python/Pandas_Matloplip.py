import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("danh_sach_1000_san_pham.xlsx",engine="openpyxl")

df["Tiền thu về năm (VNĐ)"] = (
    df["Đơn giá (VNĐ)"] *
    df["Số lượng bán năm"]
)
# Top 10 hàng bán chạy
top10 = df.nlargest(10, "Số lượng bán năm")

print(top10[["Tên sản phẩm", "Số lượng bán năm"]])
print("**************")

#Top 10 sản phẩm bán chậm nhất 
bottom10 = df.nsmallest(10, "Số lượng bán năm")

print(bottom10[["Tên sản phẩm", "Số lượng bán năm"]])

# Sản phẩm sắp hết hàng
sap_het_hang =df[df["Tồn kho"]<50]
print(sap_het_hang[["Tên sản phẩm", "Tồn kho"]])

#Sản phẩm tồn kho lâu
ton_lau = df[
    (df["Tồn kho"] > 500) &
    (df["Số lượng bán năm"] < 200)
]

print(ton_lau.head())

# Doanh thu theo tháng
df["Doanh thu tháng"] = (
    df["Đơn giá (VNĐ)"] *
    df["Số lượng bán tháng"]
)

tong_doanh_thu_thang = (
    df["Doanh thu tháng"].sum()
)

print(tong_doanh_thu_thang)

# Doanh thu theo danh mục sản phẩm
df["Doanh thu năm"] = (
    df["Đơn giá (VNĐ)"] *
    df["Số lượng bán năm"]
)

doanh_thu_dm = (
    df.groupby("Danh mục")["Doanh thu năm"]
    .sum()
    .sort_values(ascending=False)
)

print(doanh_thu_dm)

# Tỷ lệ tăng trưởng doanh thu
doanh_thu_thang_truoc = 500000000
doanh_thu_thang_nay = 650000000

ty_le = (
    (doanh_thu_thang_nay -
     doanh_thu_thang_truoc)
    / doanh_thu_thang_truoc
) * 100

print(f"{ty_le:.2f}%")

# Giá trị hàng tồn kho
df["Giá trị tồn kho"] = (
    df["Đơn giá (VNĐ)"] *
    df["Tồn kho"]
)

tong_gia_tri = df["Giá trị tồn kho"].sum()

print(
    f"Tổng giá trị tồn kho: {tong_gia_tri:,.0f} VNĐ"
)

# Dự báo nhu cầu sản phẩm
df["Nhu cầu tháng tới"] = (
    df["Số lượng bán năm"] / 12
).round()


# Lợi nhuận ước tính theo sản phẩm
df["Giá vốn"] = (
    df["Đơn giá (VNĐ)"] * 0.7
)

df["Lợi nhuận"] = (
    (df["Đơn giá (VNĐ)"] -
     df["Giá vốn"])
    * df["Số lượng bán năm"]
)
top_profit = df.nlargest(
    10,
    "Lợi nhuận"
)
print(
    top_profit[
        ["Tên sản phẩm", "Lợi nhuận"]
    ]
)