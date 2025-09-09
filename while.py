#
# # print("Do'stlaringizni yoshini saqlaymiz!")
# # dostlar={}
# # ishora=True
# # while ishora:
# #     name=input("ismini kiriting: ").title()
# #     age=int(input("yoshini kiriting: "))
# #     dostlar[name]=age
# #     qu=input("yana kiritasizmi?  (ha/yoq)").lower()
# #     if qu=="yoq":
# #         ishora=False
# # print(dostlar)
# #
#
#
#
#
#
#
#
#
# cars=["nexia","cobalt","nexia","matiz"]
# while "nexia" in cars:
#     cars.remove("nexia")
# print(cars)


talabalar=["ali","vali","nurik","shurik"]
baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba} bahosini kiriting: ")
    print(f"{talaba} baholandi!")
    baholangan_talabalar[talaba.title()]=baho

print(baholangan_talabalar)








