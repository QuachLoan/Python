try:
    a= int(input("Nhap so a :"))
    b= int(input("Nhap so b :"))
    if(b>3):
        raise SyntaxError()
    kq=a/b
    print(kq)
except ValueError:
    print("Nhập sai")
except ZeroDivisionError:
    print("Không chia được cho số 0")
except SyntaxError:
    print("hệ thống lỗi")
except Exception as e:
    print("lỗi không xác định",e)
else:
    print("Thoat, thanh cong")
finally:
    print("Chương trình kết thúc")