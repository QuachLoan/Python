import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_excel("students.xlsx")
result= df.groupby("Lop")["Diem"].mean()
print(result)

plt.figure(figsize=(10,5))
plt.bar(result.index,result.values)

plt.title("diem trung binh theo lop")
plt.xlabel("Ten lop")
plt.ylabel("Diem TB")

plt.ylim(0,10)


# hien thi gia tri
for i,value in enumerate(result.values):
    plt.text(i,value,f"{value:.2f}",ha="center")
plt.grid(axis="y",linestyle="")


# xuat anh
plt.savefig("lophoc_diemtrungbinh.png")
plt.show()