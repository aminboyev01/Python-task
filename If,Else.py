###############1##################
m=input("Ob-havoni kiriting: ")
m=int(m)
if m<0:
    print("Sovuq🥶")
elif 0<m<=20:
    print("Salqin🙄")
elif 21<=m<=30:
    print("Iliq👌")
else:
    print("Issiq🥵")
###############2##################
m=int(input("Xarid summasini kiriting: "))
if m<50000:
    print("Chegirma yo'q")
elif 50000<=m<=100000:
    print("5% chegirma bor!")
    print(m-(5/100)*m)
else:
    print("10% chegirma bor!")
    print(m-(10/100)*m)


#############3####################
login=input("Loginni kiriting: ").lower()
parol=input("Parolni kiriting: ")
if login=="admin"and parol=="12345":

    print("Xush kelibsiz!")
else:
    print("Login yoki parol xato")

##############4###################
age=int(input("Yoshingizni kiriting: "))
if age<13:
    print( "Sizga ushbu film tavsiya etilmaydi")
elif 13<=age<=17:
    print( "Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
else:
    print("Siz filmni tomosha 16qilishingiz mumkin")

##############5###################
print('''1-Osh
2-Mastava
3-Shashlik''')
tanlov=input("Tanlovingiz: ").lower()
if tanlov=="osh":
    print("Narxi: 30 ming\nTayyorlanish vaqti:20 min")
elif tanlov=="mastava":
    print("Narxi: 45 ming\nTayyorlanish vaqti:30 min")
elif tanlov=="shashlik":
    print("Narxi: 25 ming\nTayyorlanish vaqti:25 min")
else:
    print("Bunday taom ro'yxatda mavjud emas ")

##############6###################
email=input("Emailni kiriting: ")
if email.find("@")+1>0 and email.find(".")+1>0:
    print("Email qabul qilindi")
else:
    print("Noto'g'ri email manzili")

##############7####################
ball=int(input("Balingizni kiriting (0-100): "))
if ball<=0 or ball>100:
    print("Balni 0-100 oraliqda kiriting")
elif ball<55:
    print("2 baho")
elif 55<=ball<=69:
    print("3 baho")
elif 70<=ball<=85:
    print("4-baho")
else:
    print("5 baho")
#############8######################
karta=int(input("Karta mablag'i: "))
summ=int(input("Yechilmoqchi bo'lgan summani kiriting: "))
if summ>=karta:
    print("Kartada bunday mablag' mavjudmas")
elif summ<5000:
    print("Minimal 5000 sum kiriting")
elif karta>summ:
    print("Pul muvaffaqiyatli yechildi")
    print(f"Kartada {karta-summ-summ/100} sum qoldi")
else:
    print("Raqamda kiriting")
###############9#########################
print('''Hafta kunlari:
"Dushanba"
"Seshanba"
"Chorshanba"
"Payshanba"
"Juma"
"Shanba"
"Yakshanba"''')
user=input("Hafta kunini kiriting: ").lower()
if user=="yakshanba" or user=="shanba":
    print("Bugun dam olish kuni!")
elif user=="dushanba" or user=="seshanba" or user=="chorshanba" or user=="payshanba" or user=="juma":
    print("Ish kuni bugun")
else:
    print("Hafta kunini kiriting (Dushanba, Seshanba, Chorshanba,\n Payshanba, Juma, Shanba, Yakshanba)")

##################10##########################
t = input("Oyiga qancha internet trafik ishlatasiz? (GB): ")
try:
    gb = float(t.replace(',', '.').strip())
    if gb < 1:
        print("Sizga 'Mini' tarifi mos keladi")
    elif gb <= 5:
        print("Sizga 'Standard' tarifi mos keladi")
    else:
        print("Sizga 'Unlimited' tarifi mos keladi")
except:
    print("Iltimos, raqam kiriting (masalan, 3.5)")








































