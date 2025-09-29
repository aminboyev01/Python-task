
class Talaba:
    __jami_talaba=0

    def __init__(self,ism,familiya,yosh,manzil,Tel):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.__manzil=manzil
        self.__Tel=Tel
        Talaba.__jami_talaba+=1


    def talaba_info(self):
        return f"Ismi: {self.ism}\nFamiliya: {self.familiya}\nYosh: {self.yosh}\nManzil: {self.__manzil}\nTel: {self.__Tel}\n"


    def set_manzil(self,manzil):
        if manzil.isalpha():
            self.__manzil=manzil
        else:
            print("Faqat matn kiriting! ")


    def Select_manzil(self):
        return self.__manzil


    def set_Tel(self,Tel):
        if str(Tel).isdecimal():
            self.__Tel=Tel
        else:
            print("Faqat raqam kiriting! ")


    def Select_tel(self):
        return self.__Tel


    @classmethod
    def jami_talaba(cls):
        return cls.__jami_talaba


    @classmethod
    def Talaba_baholar(cls,fizika,matematika,ingliztili,onatili,tarix):
        cls.fizika=fizika
        cls.matem=matematika
        cls.ingliz=ingliztili
        cls.onatil=onatili
        cls.tarix=tarix
        return f"fizika:{cls.fizika}\nmatematika:{cls.matem}\ningliztili:{cls.ingliz}\nonatili:{cls.onatil}\ntarix:{cls.tarix}"

##########################################################################

abyekt1=Talaba("shohrux","Aminboyev",19,"xorazm",932042530)
abyekt2=Talaba("shahzod","Masharipov",19,"Toshkent",991650327)

print(abyekt1.talaba_info())

abyekt1.set_Tel(999999999)
print(abyekt1.Select_tel())

abyekt1.set_manzil("Xonqa")
print(abyekt1.Select_manzil())

print(Talaba.jami_talaba())

print(Talaba.Talaba_baholar(3,4,5,5,4))

