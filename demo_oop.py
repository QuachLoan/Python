from OOP.obj import Student
from OOP.Numbers import PhanSo
sv1= Student("sv001","Nguyen Van An","t2605e",9)
sv2= Student("sv002","Nguyen Van B","t2605e",10)
print(sv1.an_com())
print(sv1.xep_loai())
print(sv1.Diem)
Student.thong_bao()
data={
    "Msv":"SV004",
    "HoTen":"Nguyen Van An",
    "Lop":"t2605e",
    "Diem":6
}
sv4= Student.from_dict(data)
import pandas as pd
df= pd.read_excel("students.xlsx")
ds=[]
for _, row in df.iterrows():
    d= row.to_dict()
    sv= Student.from_dict(d)
    ds.append(sv)
# viet 1 lop PhanSo gom 2 thuoc tinh tu so va mau so
# va cac hanh vi(method): cong 2 phan so , tru 2 phan so ,nha 2 phan so ,chia 2 phan so
# Ps1= PhanSo(3,2)
# Ps2= PhanSo(3,2)
# print(PhanSo.add(Ps1,Ps2))
# print(PhanSo.tru(Ps1,Ps2))
# print(PhanSo.nhan(Ps1,Ps2))
