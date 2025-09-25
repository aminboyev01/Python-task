class Avto:
    def __init__(self,model,rang,karobka,yili,probeg,narx):
        self.model=model
        self.rang=rang
        self.karobka=karobka
        self.yil=yili
        self.probeg=probeg
        self.narx=narx


    def xususiyatlar(self):
        print('''Xususiyatlar: model,rang,karobka,yili,probeg,narx\n''')

    def get_info(self):
        print(f"Modeli: {self.model}\nRangi:{self.rang}\nYili: {self.yil}\nProbegi: {self.probeg}\n")

    def update_probeg(self,km):
        self.probeg+=km
        return f"Yangi probegi: {self.probeg}\n"

    def update_narx(self,narx):
        self.narx=narx
        return f"{self.model}ning yangi narxi: {self.narx}\n"
abyekt1=Avto("cobalt","qizil","avtomat",2023,6000,160000000)
abyekt1.xususiyatlar()
abyekt1.get_info()
print(abyekt1.update_narx(170000))
print(abyekt1.update_probeg(200))
