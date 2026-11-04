import pandas as pd

data={
    "Msv":["SV001","SV002","SV003"],
    "HoTen":["Nguyen Van A","Nguyen Van B","Nguyen Van C"],
    "Lop":["11","12","13"],
    "Diem":[6,7,8]
}

df= pd.DataFrame(data)
df.to_excel("students.xlsx",index=False)
print("Done")