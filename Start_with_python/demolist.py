# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_numbers=[]
# for n in numbers:
#     if n%2==0:
#         even_numbers.append(n)
# print(even_numbers)
# # list conprehension
# even_numbers=[n for n in numbers if n%2==0]

# tao list cac so nguyen to tu 1->100
# def so_nguyen_to(n):
#     if n<2:
#         return False
#     for i in range (2,n):
#         if n%i==0:
#             return False
#     return True
# ds_snt=[n for n in range(1,100) if so_nguyen_to(n)]
# print(ds_snt)
# new_list = [new value for item in interable if condition]
# dictionary nhu object

prodcuts={
    "latest":{
        "name":"Iphone 17",
        "price":1000
    },
    "best seller":{
        "name":"Iphone 17",
        "price":1500
    }
}
with open("product.txt","w",encoding="utf-8") as f:
    for key,data in prodcuts.items():
        f.write(f"{data['name']}\n")
print("da ghi du lieu vao filter")