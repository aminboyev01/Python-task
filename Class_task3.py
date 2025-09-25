class Avtosalon:
    def __init__(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.avtomobillar = []

    def qo_shish(self, model, rang, yil, narx):
        avto = {
            "model": model,
            "rang": rang,
            "yil": yil,
            "narx": narx
        }
        self.avtomobillar.append(avto)

    def avto_info(self):
        if not self.avtomobillar:
            return "Salonda hozircha avtomobil yo‘q."
        info = f"{self.salon_nomi} ({self.manzili}) dagi avtomobillar:\n"
        for i, avto in enumerate(self.avtomobillar, 1):
            info += (f"{i}) Model: {avto['model']}, Rang: {avto['rang']}, "
                     f"Yil: {avto['yil']}, Narx: {avto['narx']} so'm\n")
        return info

    def holat(self):
        return f"Salonda jami {len(self.avtomobillar)} ta avtomobil mavjud."

    def manzil_info(self):
        return f"Avtosalon: {self.salon_nomi}, Manzil: {self.manzili}"


salon = Avtosalon("GM Avtosalon", "Xorazm, Bog‘ot")
salon.qo_shish("Cobalt", "oq", 2023, 170000000)
salon.qo_shish("Spark", "qora", 2022, 100000000)
salon.qo_shish("Malibu", "qizil", 2024, 300000000)

print(salon.manzil_info())
print(salon.holat())
print(salon.avto_info())
