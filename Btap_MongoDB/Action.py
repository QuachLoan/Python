from pymongo import MongoClient
import pandas as pd
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")

db = client["T2605E"]

products = db["Products"]

orders = db["Orders"]

def hien_thi_san_pham():

    print("\nDANH SACH SAN PHAM")

    for p in products.find({}, {"_id":0}):

        print(
            p["MaSP"],
            p["TenSP"],
            p["Gia"],
            p["SoLuong"]
        )
def tim_kiem():

    keyword = input("Nhap ten san pham: ")

    result = products.find(
        {
            "TenSP":{
                "$regex":keyword,
                "$options":"i"
            }
        },
        {"_id":0}
    )

    for p in result:
        print(p)
def them_san_pham():

    sp = {
        "MaSP": input("Ma SP: "),
        "TenSP": input("Ten SP: "),
        "Gia": float(input("Gia: ")),
        "SoLuong": int(input("So luong: "))
    }

    products.insert_one(sp)

    print("Them thanh cong")
def cap_nhat_gia():

    ma = input("Nhap ma SP: ")

    gia = float(input("Gia moi: "))

    products.update_one(
        {"MaSP":ma},
        {
            "$set":{
                "Gia":gia
            }
        }
    )

    print("Cap nhat thanh cong")
def lap_don_hang():

    ma_dh = input("Ma don hang: ")

    chi_tiet = []

    tong_tien = 0

    while True:

        ma_sp = input("Ma SP (0 de dung): ")

        if ma_sp == "0":
            break

        sp = products.find_one({"MaSP":ma_sp})

        if not sp:
            print("Khong tim thay")
            continue

        sl = int(input("So luong: "))

        thanh_tien = sl * sp["Gia"]

        tong_tien += thanh_tien

        chi_tiet.append(
            {
                "MaSP":sp["MaSP"],
                "TenSP":sp["TenSP"],
                "SoLuong":sl,
                "DonGia":sp["Gia"],
                "ThanhTien":thanh_tien
            }
        )

        products.update_one(
            {"MaSP":ma_sp},
            {
                "$inc":{
                    "SoLuong":-sl
                }
            }
        )

    order = {
        "MaDH":ma_dh,
        "NgayLap":str(datetime.now()),
        "TongTien":tong_tien,
        "ChiTiet":chi_tiet
    }

    orders.insert_one(order)

    print("Lap don thanh cong")
def hien_thi_hoa_don():

    ma = input("Nhap ma don hang: ")

    order = orders.find_one(
        {"MaDH":ma},
        {"_id":0}
    )

    if not order:
        return

    print("\nHOA DON")

    print("Ma DH:", order["MaDH"])

    print("Tong tien:", order["TongTien"])

    for item in order["ChiTiet"]:

        print(
            item["TenSP"],
            item["SoLuong"],
            item["ThanhTien"]
        )
def xem_don_hang():

    for o in orders.find({}, {"_id":0}):

        print(
            o["MaDH"],
            o["NgayLap"],
            o["TongTien"]
        )
def thong_ke_doanh_thu():

    ds = list(
        orders.find(
            {},
            {
                "_id":0,
                "TongTien":1
            }
        )
    )

    tong = sum(
        x["TongTien"]
        for x in ds
    )

    print("Tong doanh thu:", tong)
def export_products():

    data = list(
        products.find(
            {},
            {"_id":0}
        )
    )

    df = pd.DataFrame(data)

    df.to_excel(
        "products_export.xlsx",
        index=False
    )

    print("Da xuat products")
def export_orders():

    data = list(
        orders.find(
            {},
            {"_id":0}
        )
    )

    df = pd.DataFrame(data)

    df.to_excel(
        "orders_export.xlsx",
        index=False
    )

    print("Da xuat orders")
