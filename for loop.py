# #1
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for gmail in pochtalar:
#     num=gmail.find("@")+1
#     if num>0:
#         print(f"Tog'ri email: {gmail} \n @-indeksi: {num-1 } ")
#     else:
#         print(f"Notog'ri email: {gmail} ")
# #################################################
# #2
# parol=["password123", "Qwerty!", "admin", "StrongPass1!"]
# for par in parol:
#     if len(par)<8:
#         print("Parol qisqa😒")
#     elif par.isalpha():
#         print("Kuchsiz parol😒")
#     else:
#         print("Kuchli parol💀")
# #################################################
# #3
# harorat=[20, 22, 19, 24, 25, 23, 21]
# print("Haftalik havo malumoti: ")
# for har in harorat:
#     if har>22:
#         print(f"{harorat.index(har)+1}-kun: Iliq havo")
#     else:
#         print(f"{harorat.index(har)+1}-kun: Sovuq havo")
# print(f"Haftalik o'rtacha harorat:{sum(harorat)/len(harorat)} ")
#
# ######################################################
# #4
# meal=["Osh", "Shashlik", "Manti","Lagmon"]
# buyurtma=input("Ovqat nomi: ").title()
# if buyurtma in meal:
#     print(" Buyurtmangiz qabul qilindi ")
# else:
#     print( "Kechirasiz, bunday taom yo'q" )
# ##########################################
# #5
# yosh=[16, 21, 17,30,25]
# for age in yosh:
#     if age<18:
#         print("Yosh chegarasiga yetmagan")
#     else:
#         print("Xush kelibsiz" )
#
# ##########################################
# #6
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for i in xabarlar:
#     if i== "Batareya past":
#         print("Telefoningizni quvvatlang!! ")
#
# ##########################################
# #7
fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
music=[]
photo=[]
for tur in fayllar:
    if tur.find(".jpg",-1,-3)>0:
        photo.append(tur)
    else:
        music.append(tur)
print(music)
print(photo)

#
# m=("salom "
#    "dunyo")
# if "a" in m:
#     print(":bor ")
#
#















