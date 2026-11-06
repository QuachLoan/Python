# Quản lý điểm học sinh, lớp có 10 học sinh
# Viết chương trình quản lý điểm của 3 môn học Toán, Lý Hoá
# Menu theo chưucs năng kiểu:
# Nhập họ tên học sinh
# Nhập điểm Toán Lý Hoá
# Lựa chọn in kết quả thống kê của lớp:
    # Số lượng học sinh
    # Số lượng học sinh XS/Giỏi/Khá/TB/Yếu
    # Điểm  tb học sinh cao nhất/ thấp nhất
    # TB của cả lớp

ten = []
dtb = []

for i in range(2):
    print(f"\nNhập thông tin học sinh thứ {i+1}")

    ten_hs = input("Tên: ")
    toan = float(input("Toán: "))
    ly = float(input("Lý: "))
    hoa = float(input("Hóa: "))

    diem_tb = (toan + ly + hoa) / 3

    ten.append(ten_hs)
    dtb.append(diem_tb)

# Thống kê
xs = gioi = kha = tb = yeu = 0

for diem in dtb:
    if diem >= 8:
        xs += 1
    elif diem >= 6.5:
        gioi += 1
    elif diem >= 5:
        kha += 1
    elif diem >= 3.5:
        tb += 1
    else:
        yeu += 1

print("\n===== THỐNG KÊ LỚP =====")
print("Số lượng học sinh:", len(ten))
print("Số HS Xuất sắc:", xs)
print("Số HS Giỏi:", gioi)
print("Số HS Khá:", kha)
print("Số HS Trung bình:", tb)
print("Số HS Yếu:", yeu)

print("Điểm TB cao nhất:", max(dtb))
print("Điểm TB thấp nhất:", min(dtb))
print("Điểm TB cả lớp:", sum(dtb) / len(dtb))
