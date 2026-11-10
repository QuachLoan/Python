# lam viec voi mongodb...
import pandas as pd
from OOP.obj  import Student
from workWithMongoDB.Database.MongoDB import MongoDB
# lay sinh vien tu file excel
df = pd.read_excel("students.xlsx")
ds = []
for _, row in df.iterrows(): # duyet df
    d = row.to_dict() # chuyen row thanh dict
    sv = Student.from_dict(d) # chuyen dict thanh object Student
    ds.append(sv) # them sv vao danh sach
# import vao db
db = MongoDB()
db.kiem_tra_ket_not()
print("Ket noi MongoDB thanh cong")
collection = db.collection
data = [sv.to_dict() for sv in ds] # chuyen danh sach object thanh danh sach dict
collection.insert_many(data) # import vao db