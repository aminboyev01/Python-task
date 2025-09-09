# talaba={"ism":"shohrux",
#         "familiya":"Aminboyev",
#         "yosh":19,
#         "manzil":"xorazm",
#         "tuman":"bog'ot"
#         }
# # print(talaba.items())
# # print(type(talaba.items())
# # for key,value in talaba.items():
# #     print(f"Key: {key}")
# #     print(f"Value: {value}\n")
#
# # #
# # for key in talaba:
# #     print(f"keys: {key}")
#
# #
# #
#
# # print(talaba["ism"])
#
#
#


#
# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# bozorlik=["olma","uzum","shaftoli"]
# for mahsulot in sorted(mahsulotlar):
#     if mahsulot in bozorlik:
#         print(f"mahsulot: {mahsulot}\nnarxi: {mahsulotlar[mahsulot]}")
#
#     else:
#         print(f"mahsulot {mahsulot} bozorlikda yoq")
#
#
# #
# # print(mahsulotlar.items())
#
#
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
#     }
# for phone in set(telefonlar.values()):
#     print(phone)
#
# #
# #
# #
# #
# #
# #
#
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }
# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }
# cars=[car0,car1]
# print(cars[1]['korobka'])
# print(cars[0]['rang'])
# print(cars[0]['model'])
#
#
# #
# #
# #
#
#
# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)
# for car in malibus[:3]:
#     car['rang']='qizil'
# for car in malibus[3:6]:
#     car['rang']='boqrang'
# for car in malibus[6:]:
#     car['korobka']='mexanik'
# for car in malibus:
#     if car['korobka']=="avto":
#         print(f"{car} narxi: 40.000$")
#     else:
#         print(f"{car} narxi: 35.000$")
# print(malibus)
#
#
# #
# #
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
# for ism,tillar in dasturchilar.items():
#     print(f"{ism} quyidagi tillarni biladi: ")
#     for til in tillar:
#         print({til})
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
#
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# a=["ism","yosh","kurs","mol"]
# new_dict=dict.fromkeys(a,12)
# print(new_dict)
#
#
# b=["salom","shohrux","ee"]
# new_d=dict.fromkeys(b,"keldingmi?")
#
# print(new_d)
#
#
#
# aa=dict(s=1,d=2,)
# print(aa)
#
#
#
#
# key=["ism","shohrux","yosh"]
# value=["shohrux","zor bola",19]
# l=dict(zip(key,value))
# print(l)
#
#
# ll={"ism":"shohrux","yosh":19}
# m=ll.setdefault("ism","sj")
# print(m)
# print(ll)
#
#





#
#
#
#
# ss={True,1,True,1}
#
# print(ss)
#
#
#
#
# # my_set={"apple","banana","cherry",1,2}
# # print(my_set)
# # thisset=set(("salom","alik","nima","gap"))
# # print(thisset)
#
# son=1
# while son<=5:
#     print(son,end=" ")
#     son+=1
#
#
#
# print("Kiritilgan sonni kvadratini topuvchi dastur: \n")
# savol="istalgan son kiriting"
# savol+="dasturdan chiqish uchun exit ni bos!\n"
# ishora=True
# qiymat=input(savol)
# if qiymat=="exit":
#     ishora=False
# else:
#     print(float(qiymat)**2)























































