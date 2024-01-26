#faylni ochish uchun
# file = open(file="15-dars. Fayllar/royhat.txt",mode="r")
# malumot = file.readline()
# print(malumot)
# malumot = file.readline()
# print(malumot)
# malumot = file.readline()
# print(malumot)
# malumot = file.readline()
# print(malumot)
# while True:
#     malumot = file.readline()
#     print("line ",malumot,end="")
#     if not malumot:
#         break
# malumot = file.readlines()
# print(malumot)
# file.close() #faylni yopadi
# print(file.closed)
# print(malumot)

# file = open("dars.txt","w")
# file.write("Salom\nBugun juma!")
# file.close()

# for i in range(1000000):
#     file = open(f"dars/dars-{i+1}.txt","w")
#     file.write("salom")

# with open("dars.txt","a") as file:
#     file.write("\nBugun Juma")

#mode 
#r - read(o'qish uchun)
#w - write(yozish uchun)
#a - append(davomidan qo'shish uchun)
#x - file do not exsist(fayl yaratilmagan bo'lsa)
#r+, w+ ,a+, binar - rb, wb, ab

# import requests

# response = requests.get("https://cataas.com/cat")
# content = response.content

# with open(file="cat.jpg",mode="wb") as file:
#     file.write(content)

cat = open("cat.jpg","rb").read()

with open(file="cat-copy.jpg",mode="wb") as file:
    file.write(cat)