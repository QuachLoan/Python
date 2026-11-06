import pandas as pd
# df= pd.read_excel("students.xlsx")
# print(df)
# print("Done")
# avg= df["Diem"].mean()
# print("Diem trung binh :",avg)
# best = df.loc[df["Diem"].idxmax()]
# print(best)
# good=df.loc[df["Diem"]>=8]
# print("Hoc sinh tot nhat :",good)
# result = df.groupby("Lop")["Diem"].agg(["count","mean","max","min"])
# print(result)

df=pd.read_excel("students.xlsx")
print(df)

avg= df["Diem"].mean()
print(avg)
best= df.loc[df["Diem"].idxmax()]
print(best)
good=df.loc[df["Diem"]>=3]
print(good)

result= df.groupby("Lop")["Diem"].agg(["count","mean","max","min"])
print(result)