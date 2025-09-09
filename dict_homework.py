#1
new_dict={
    "Boolen":"Mantiqiy qiymay",
    "Float":"O'nlik son",
    "For":"Biror amalni qayta bajarish tsikli",
    "If":"Shartni tekshirish operatori",
    "integer":"Butun son"

}
for key in sorted(new_dict.keys()):
    print(f"{key}:{new_dict[key]}")

#2
new_dict={
    "AQSH":"Washinton",
    "ITALIYA":"Rim",
    "MALAZIYA":"KUALA-LUMPUR",
    "O'ZBEKISTON":"TOSHKENT",
    "ROSSIYA":"MOSKVA",
    "SINGAPUR":"SUNGAPUR",
    "QOZOG'IZTON":"BISHKEK",

}
for key in sorted(new_dict.keys()):
    print(key)

print("######################################")
for value in sorted(new_dict.values()):
    print(value)



#3
w_dict={
    "AQSH":"Washinton",
    "ITALIYA":"Rim",
    "MALAZIYA":"KUALA-LUMPUR",
    "O'ZBEKISTON":"TOSHKENT",
    "ROSSIYA":"MOSKVA",
    "SINGAPUR":"SUNGAPUR",
    "QOZOG'IZTON":"BISHKEK",

}
user=input("Qaysi davlatni poytaxti kerak: ").upper()
if user in w_dict:
    print(f"{user}ni poytaxti: {w_dict[user]}")
else:
    print("Kechirasiz, bizda bunday malumot yoq")
#4
new_dict={
    "Oyim":["titanic","interstellar","shumbola"],
    "dadam":["cho'qintirgan ota","shum bola","shovkebtdan qochish"],
    "o'zim":["Bread box","The last of use","Platform"],
    "Apkam":["Bilimman"]
}
for keys,values in new_dict.items():
    print(f"\n{keys}ni sevimli kinosi:")
    for value in values:
        print(f"{value}")

#5
davlatlar = {
    "O'zbekiston": {
        "hududi": "448.9 ming km²",
        "aholisi": "36 mln",
        "pul_birligi": "so'm"
    },
    "AQSH": {
        "hududi": "9.8 mln km²",
        "aholisi": "333 mln",
        "pul_birligi": "dollar"
    },
    "Rossiya": {
        "hududi": "17.1 mln km²",
        "aholisi": "146 mln",
        "pul_birligi": "rubl"
    },
    "Xitoy": {
        "hududi": "9.6 mln km²",
        "aholisi": "1.4 mlrd",
        "pul_birligi": "yuan"
    },
    "Hindiston": {
        "hududi": "3.2 mln km²",
        "aholisi": "1.4 mlrd",
        "pul_birligi": "rupi"
    },
    "Turkiya": {
        "hududi": "783 ming km²",
        "aholisi": "85 mln",
        "pul_birligi": "lira"
    },
    "Qozog'iston": {
        "hududi": "2.7 mln km²",
        "aholisi": "20 mln",
        "pul_birligi": "tenge"
    },
    "Fransiya": {
        "hududi": "643 ming km²",
        "aholisi": "67 mln",
        "pul_birligi": "yuro"
    },
    "Germaniya": {
        "hududi": "357 ming km²",
        "aholisi": "83 mln",
        "pul_birligi": "yuro"
    },
    "Yaponiya": {
        "hududi": "378 ming km²",
        "aholisi": "125 mln",
        "pul_birligi": "yen"
    }
}

for davlat,info in davlatlar.items():
    print(f"\n{davlat} haqida malumot:")
    for v,z in info.items():
        print(f"{v}:{z}")





















































































