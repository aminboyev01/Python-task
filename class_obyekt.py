class Fanla:
    def __init__(self,**kwargs):
        self.matematika=kwargs.get("matematika",0)
        self.Fizika=kwargs.get("Fizika",0)
        self.Tarix=kwargs.get("Tarix",0)
        self.ingliztili=kwargs.get("ingliztili",0)
        self.fanlar_dict=kwargs


    def baholar(self):
        print("Baholar:")
        for key,value in self.fanlar_dict.items():
            print(f"{key}: {value}")


    def fanlar_soni(self):
        A=len(self.fanlar_dict)
        return f"Sizda {A} ta fan mavjud\n"


    def alo_baho(self):
        print(f"Shu fanlarni yaxshi ozlashtirdingiz!")
        for key, value in self.fanlar_dict.items():
            if value==5:
                print(f"{key}: {value}\n")


    def past_baho(self):
        print(f"Shu fanlarni ozlashtira olmadingiz!")
        for key, value in self.fanlar_dict.items():
            if value==3:
                print(f"{key}: {value}\n")


    def ortacha_baho(self):
        n=0
        qiymat=0
        for  value in self.fanlar_dict.values():
            qiymat+=value
            n+=1
        ortacha_qiy=qiymat/n
        return f"O'rtacha baho: {ortacha_qiy}\n"


    def fan_olibtashla(self,f):
        if f in self.fanlar_dict:
            print(f"{f} fani olib tashlandi\n")
            del self.fanlar_dict[f]

        else:
            print(f"{f} topilmadi\n")


    def fan_qoshish(self,key,value):
        self.fanlar_dict[key]=value
        print(f"{key} fani qoshildi!\n")


abyekt1=Fanla(matematika=5,Fizika=4,Tarix=3,ingliztili=2)
# abyekt1.fan_qoshish("Ingliztili",5)
# abyekt1.baholar()
# print(abyekt1.fanlar_soni())
# abyekt1.alo_baho()
# abyekt1.past_baho()
# print(abyekt1.ortacha_baho())




class Talaba(Fanla):
    def __init__(self,ism,familiya,yosh,kursi,**kwargs):
        super().__init__(**kwargs)
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.kursi=kursi
        self.fanlar=self.fanlar_dict


    def Talaba_info(self):
        return f"Ism Familiya: {self.familiya} {self.ism}\nKursi: {self.kursi},\nYoshi: {self.yosh}da"


    def Fan_lar(self):
        print(f"{self.fanlar_soni()}")


    def Fan_korish(self):
        return self.baholar()


    def Talaba_ortbal(self):
        print("Talaba"+self.ortacha_baho())


abyekt2=Talaba("shohrux","Aminboyev",19,2, matematika=5, Fizika=4, Tarix=3, ingliztili=4)
print(abyekt2.Talaba_info())
abyekt2.Fan_lar()
abyekt2.Fan_korish()
abyekt2.Talaba_ortbal()





































