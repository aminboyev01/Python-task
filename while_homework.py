import random
#1
while True:
    rang=input("svitafor qaysi rangda: ").lower()
    if rang=="qizil" or rang=="yashil" or rang=="sariq":
        print("Tog'ri!")
        break
    else:
        print("Xato rang")

#2
print("Kompyuter 1 dan 10 gacha bo'lgan tasodifiy son o'ylaydi siz uni toping!\n")

while True:
    sanash = 1
    taxmin_son = random.randint(1, 10)
    ishora = True
    while ishora:

        javob = input("Sonni kiriting: ")
        if taxmin_son == int(javob):
            print("Topdingiz qoyil!!!")
            print(f"{sanash}ta imkonyatda topildi")
            sanash += 1
            ishora = False
        else:
            print("Qayta urining")
            print(f"{sanash}-imkoniyat ketti")
            sanash += 1
    javob1=input("qayta o'ynaysizmi: ").lower()
    if javob1=="ha" or javob1=="ova":
        ishora=True
        sanash=1
        continue
    else:
        print("O'yin tugadi! ")
        break


#3
lis=[]
while True:
    qiymat=input("Do'stingizni ismini kiriting: ")

    if  qiymat=="stop":
        print("Sikl Toxtadi")
        break
    lis.append(qiymat)

print(lis)


#4
USD=12600
print(f"1$={USD}\n")
print('''<< Sumni => $ ga aylantirish uchun-1 >>
<< $ => sumga bolsa-2 >>\n''')
while True:
    qiymat=input("kiriting: ")

    if qiymat=="exit":
        break
    if qiymat=="1":
        pul = int(input("narxni kiriting: "))
        print("sum => $")
        result=pul/USD
        print(f"{pul}sum =>{result}$")
    elif qiymat=="2":
        pul = int(input("narxni kiriting: "))
        print("$ => sum")
        result=pul*12600
        print(f"{pul}$=> {result}sum")
    else:
        print("Faqat 1 yoki 2 ni kiriting!")











