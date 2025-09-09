import random

print("""Kompyuter o'ylagan sonni topuvchi dastur!
Kompyuter o'ylagan sonni toping!\n""")

while True:
    m = int(input("Kompyuter son boshlang'ich chegarasi: "))
    d = int(input("Kompyuter son oxirgi chegarasi: "))
    imkoniyat = int(input("Topish uchun imkoniyat: "))

    taxmin_son = random.randint(m, d)
    sanash = 1

    while sanash <= imkoniyat:
        son = int(input("Sonni kiriting: "))

        if son > d or son < m:
            print(f"{m} va {d} orasida son kiriting!\n")
        elif son > taxmin_son:
            print("Kichikroq son!\n")
        elif son < taxmin_son:
            print("Kattaroq son!\n")
        else:
            print(f"{sanash}-urinishda topdingiz!!! 🎉")
            break

        print(f"{sanash}-imkoniyat ketdi\n")
        sanash += 1
    else:
        print("Imkoniyat tugadi! 😢")

    e = input("Yana o'ynaysizmi? (ha/yo‘q): ").lower()
    if e != "ha" and e != "ok":
        print("O‘yin tugadi!")
        break
