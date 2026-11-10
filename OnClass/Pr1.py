import pandas as pd
DonHang= pd.read_excel("Thuc_hanh_Python_Ban_hang.xlsx",sheet_name="DonHang")
SanPham= pd.read_excel("Thuc_hanh_Python_Ban_hang.xlsx",sheet_name="SanPham")
CuaHang= pd.read_excel("Thuc_hanh_Python_Ban_hang.xlsx",sheet_name="CuaHang")

print(DonHang.head(5))
print(CuaHang.head(5))
print(SanPham.head(5))


merge_1 = pd.merge(DonHang,CuaHang,on="MaCH",how="left")
tong_giao_dich =merge_1.groupby("TenCuaHang").size().reset_index(name="SoLuong")
    
print(tong_giao_dich)


merge_sp = pd.merge(DonHang, SanPham, on="MaSP", how="left")
merge_2 = pd.merge(merge_sp, CuaHang, on="MaCH", how="left")
danh_sach_cot=["MaDH","MaSP","NhomHang","DonGia","TenCuaHang","TinhThanh"]
kq= merge_2[danh_sach_cot]
print(kq)


dong_trung = DonHang[DonHang.duplicated(subset=["MaDH"],keep=False)]
print(dong_trung)


DonHang["Ngay_Ban_Chuyen_Doi"]= pd.to_datetime(DonHang["NgayBan"],format="%d/%m/%Y",errors="coerce")

ngay_loi = DonHang[DonHang["Ngay_Ban_Chuyen_Doi"].isna()] # nhat ra cac dong naN


if not ngay_loi.empty:

  print(ngay_loi[["MaDH", "NgayBan", "KhachHang"]])
  print(f"\nTổng số dòng có ngày không hợp lệ: {len(ngay_loi)} dòng.")
else:
  print("Tat ca hop le")

DonHang["So_luong_Chuyen_Doi"] = pd.to_numeric( DonHang["SoLuong"], errors="coerce")
DonHang["TyLe_Chuyen_Doi"]= pd.to_numeric(DonHang["TyLeGiamGia"],errors="coerce")

so_luong_loi = DonHang[DonHang["So_luong_Chuyen_Doi"].isna()]
if  not so_luong_loi.empty:
    print(so_luong_loi[["MaDH", "SoLuong", "KhachHang"]])
    print(f"\n tong so dong co ngay khong hop le :{len(so_luong_loi)} dong.")
else:
    print("tat ca hop le")

ty_le_chuyen_doi_loi = DonHang[DonHang["So_luong_Chuyen_Doi"].isna()]
if not ty_le_chuyen_doi_loi.empty:
    print(ty_le_chuyen_doi_loi[["MaDH", "TyLeGiamGia", "KhachHang"]])
    print(f"\n tong so dong co ngay khong hop le :{len(ty_le_chuyen_doi_loi)} dong.")
else:
    print("tat ca hop le")


# loi_trong = DonHang[
#     DonHang["KhachHang"].isna()
#     | DonHang["SoDienThoai"].isna()
#     | DonHang["MaSP"].isna()
# ]

# print("\n Đơn hàng bị trống tên khách hàng, số điện thoại hoặc mã sản phẩm:")
# if not loi_trong.empty:
#   print(loi_trong[["MaDH", "KhachHang", "SoDienThoai", "MaSP"]])
# else:
#   print("-> Không có lỗi (Không có ô nào bị bỏ trống ở các cột này).")


# DonHang["SoDienThoai_Str"] = DonHang["SoDienThoai"].astype(str).str.strip()

# dinh_dang_chuan = r"^0\d{9}$"

# loi_sdt = DonHang[
#     (~DonHang["SoDienThoai_Str"].str.match(dinh_dang_chuan))
#     & (DonHang["SoDienThoai"].notna())
# ]

# print("\n Đơn hàng có Số điện thoại không hợp lệ (không đủ 10 số hoặc không bắt đầu bằng 0):")
# if not loi_sdt.empty:
#   print(loi_sdt[["MaDH", "KhachHang", "SoDienThoai"]])
# else:
#   print("-> Không có lỗi (Tất cả số điện thoại hiện có đều đúng định dạng chuẩn).")

loi_trong = DonHang[DonHang["KhachHang"].isna() | DonHang["SoDienThoai"] .isna() | DonHang["MaSP"] .isna()] 
print("\n don hang bij trong ten khach hang hoac san pham")
if not loi_trong.empty:
   print()