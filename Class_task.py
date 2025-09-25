


class Foydalanuvchi:
    def __init__(self,ism,familiya,user,gmail,age):
        self.ism=ism
        self.familiya=familiya
        self.user=user
        self.gmail=gmail
        self.age=age
        self.info=[]
    def user_info(self):
        return f"Ism,Familiya:{self.familiya} {self.ism}\n"


    def info_plus(self):
        self.info.append(self.gmail)
        self.info.append(self.user)
        print("Malumotlar saqlandi!\n")

    def check_user(self):
        if self.user in self.info:
            print("User mavjud!")
        if self.gmail in self.info:
            print("Gmail mavjud!\n")

    def age_check(self):
        if self.age>=18:
            print("Siz voyaga yetgansiz!")
            print(f"Yosh: {self.age}\n")
        else:
            print("Siz hali voyaga yetmagansiz!")
            print(f"Yosh: {self.age}\n")

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
user = input("User nomini kiriting: ")
gmail = input("Gmailingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))

abyekt1=Foydalanuvchi(ism,familiya,user,gmail,age)
abyekt1.info_plus()


while True:

    print('''1-Ism Familiya
2-Ro'yxatdan o'tganlikini tekshirish
3-Yoshi haqida''')

    chance=input("Kiriting:(1:3)\n").lower()
    if chance=='1':
        print(abyekt1.user_info())
    if chance=='2':
        abyekt1.check_user()
    if chance=='3':
        abyekt1.age_check()
    if chance=="stop":
        print("Sikl toxtadi")
        
        break










