##################################### LESSON #########################

# casefold()
matn="ASSALOMU ALAYKUM yAXshiMISAn"
l=matn.casefold()
print(l)

l=["SALOM", "DUNYO","NIMA GAP"]
for m in l:
    print(m.casefold())

m="HELLO WORD"
print(m.casefold())
#####################################
# center()
matn="hi"
print(matn.center(4,"!"))

l="salom"
print(l.center(13,"!"))

m="hello word"
print(m.center(22,"@"))

#####################################
# count()
s="banana"
print(s.count("a"))

l="m1l2l3l3k3n4m5h6k7"
print(l.count("3"))

m="1234567777777"
print(m.count("7"))
# #####################################
# encode()
l="hello"
print(l.encode())

m="66557"
print(m.encode())
#####################################
# endswith()
l="salom nima"
print(l.endswith("nima"))

m="men xorazmda yashayman"
print(m.endswith("yashayman",0,22))

x="xolaga salom"
print(x.endswith("a"))


#####################################
# expandtabs()
l="salom\tdunyo nima\tgap"
print(l.expandtabs(50))

m="12\t34\t56\t78"
print(m.expandtabs(30))

k="xa\txa\txa\tmm"
print(k.expandtabs())

#####################################
# find()
l="salom"
print(l.find("o"))

m="nima gap"
print(m.find("gap"))

k="men xorazmda yashayman"
print(k.find("toshkent"))

#####################################
# format()
m="salom {} "
print(m.format("shohrux"))

k="men {}-yoshdaman va {}-kursman va {} da oqiyman"
print(k.format(19,2,"tatu"))

#####################################
# format_map()
l={"ism":"shohrux","yosh":19}
k="men {ism}man va {yosh}-yoshman "
print(k.format_map(l))

m={"kurs":2,"nom":"tatu"}
l="men {kurs}-kursman va {nom}da oqiyman".format_map(m)
print(l)

m={"joy":"xorazm","nom":"bog'ot"}
k="men {joy}dayashayman {nom}da".format_map(m)
print(k)

#####################################
# imdex()
m="men uyda yashayman".index("u")
print(m)

l="men 19 yoshdaman".index("19")
print(l)

    Demak find()-bilan farqi find xatolik bolsa -1 chiqaradi index esa error




#####################################
# isalnum()
m="helloword".isalnum()
print(m)
k="salom, alik".isalnum()
print(k)
m="1234".isalnum()
print(m)
Demak isalnum()-metodi faqat matn va raqam bolsa treu boshliq va tinish
belgilar bolsa false beradi

#####################################
#isalpha()
print("shohrux".isalpha())     #True
print("python3.11".isalpha())    #False
print("hello word".isalpha())     #False
    yani faqat harf bolsa true boshqa holatda false
#####################################
# isascii()
print("salom!".isascii())     #demak faqat ingliz harflari yani kompyuter
# tushunadigan 256 ta belgi bolsa true
print("салом".isascii())  #false

#####################################
# isdemical()
print("salom".isdecimal())
print("12346".isdecimal())
shunda faqat  0-9 oraligidagi faqat son bolsa true boshqa narsa qatnashsa false


#####################################
# isdigit()
print("12345".isdigit())     # faqat raqam → True
print("٢٣٤٥".isdigit())     # arab raqamlari → True
print("①②③".isdigit())      # maxsus raqam belgilar → True
print("123.45".isdigit())   # nuqta bor → False
print("12a34".isdigit())    # harf bor → False
isdigit() → raqam ko‘rinadigan boshqa belgilarni ham qabul qiladi (masalan, ②, ¾ kabi).

#####################################
# isidentifier()
print("ism".isidentifier())    # True
print("123salom".isidentifier()) #False
print("ism!".isidentifier())     #False
  Yani varibleni yozish daxato bolsa false togri bolsa true qaytaradi

#####################################
# Pythondagi is...() bilan boshlanadigan metodlar
# odatda  (True yoki False) qiymat qaytaradi.
#####################################
# islower()
l="salom".islower()
print(l)
l="salom11".islower()
print(l)
l="saloM".islower()
print(l)
#####################################
# isdemical()   /// isnumeric()
print("12345".isnumeric())     # oddiy raqamlar → True
print("²³".isnumeric())        # daraja belgilar ham → True
print("½".isnumeric())         # kasr belgisi → True
print("①②③".isnumeric())      # maxsus raqam belgilar → True
print("12a34".isnumeric())     # harf bor → False
print("12 34".isnumeric())     # bo'sh joy bor → False

isdecimal() → faqat oddiy 0–9 raqamlari.

isdigit() → raqam belgilarini qabul qiladi (②, ٣ va h.k.).

isnumeric() → eng keng, kasr va maxsus raqam belgilarini ham qabul qiladi (½, ² va h.k.).
#####################################
# isprintable()
print("salom dunyo".isprintable())         #true
print("salom\n dunyo \t".isprintable())    #false
yani \n \t bolsa matnda false qaytaradi
#####################################
# isspace()
print("   ".isspace())     # faqat bo'sh joy → True
print("\t".isspace())      # tab belgisi → True
print("\n".isspace())      # yangi qator belgisi → True
print(" \n\t ".isspace())  # faqat bo'sh joy belgilar → True
print(" salom ".isspace()) # ichida matn bor → False
print("123".isspace())     # raqam bor → False
yani faqat bosh joy va \n \t bolsa true

#####################################
# istitle()
print("Salom Dunyo".istitle())     # har bir so'z bosh harfi katta → True
print("Python Dasturlash Tili".istitle()) # hammasi to'g'ri → True
print("Salom dunyo".istitle())     # "dunyo" kichik bosh harf bilan → False
print("SALOM Dunyo".istitle())     # birinchi so'z hammasi katta → False
print("Shohrux".istitle())         # faqat bitta so'z, bosh harfi katta → True
  YAni title() qoidasiga mos bolsa true qolgan holatlarda false
#####################################
# isupper()
print("saloM".isupper())
print("SALOM".isupper())

  Yani barcha harflar katta bolsa true ,sonlar va tinish belgilarga qaramaydi
#####################################
# join()
l=["salom","dunyo","xaxa","pipi"]
print("-".join(l))

m=["salom","shox"]
print("! ".join(m))

LL={"SALOM","ALIK"}
print("-".join(LL))
YANI JOIN BU LIST TUPLE KABILARNI STRING QILIB CHIQARB BERAD

#####################################

#ljust()
l=" salom"
print(l.ljust(10,"#"))
ljust() faqat matndan keyingi (o‘ng tarafdagi) joylarni to‘ldiradi.
l="salom wox11"
print(l.ljust(14,"*"))

m="salom 11"
print(m.ljust(14,"%"))

k="salom dunyo"
print(k.rjust(15,"%"))
25
m=input(": ").split()
print(m)
#####################################
  # partition()
l="salom oka nima"
print(l.partition("k"))
m="124343567"
print(m.partition("3"))
BU FUNKSIYA MATNNI 3 TA BOLAKKA BOLIB BERAD BELGILAGAN JOYIMIZDAN
Xullas, partition() → stringni 3 qismga bo‘lib, ularni tuple ichida qaytaradi.
#####################################

# rfind()
print("hello world".rfind("o"))
print("banana".rfind("na"))
print("mississippi".rfind("iss"))

# rjust()
print("42".rjust(5))
print("abc".rjust(10, "-"))
print("hi".rjust(8, "*"))

# rpartition()
print("hello world".rpartition(" "))
print("banana".rpartition("na"))
print("python".rpartition("t"))

# rsplit()
print("apple,banana,cherry".rsplit(",", 1))
print("a b c d".rsplit(" ", 2))
print("hello-world-python".rsplit("-", 1))

# rstrip()
print("hello   ".rstrip())
print("bananaaaa".rstrip("a"))
print("test***".rstrip("*"))

# split()
print("apple banana cherry".split())
print("one,two,three".split(","))
print("a|b|c".split("|"))

# splitlines()
print("hello\nworld".splitlines())
print("a\nb\nc".splitlines())
print("line1\r\nline2".splitlines())

# startswith()
print("hello".startswith("he"))
print("python".startswith("py"))
print("banana".startswith("na"))

# strip()
print("   hello   ".strip())
print("****test****".strip("*"))
print("xyzabcxyz".strip("xyz"))

# swapcase()
print("Hello World".swapcase())
print("Python".swapcase())
print("mIXeD".swapcase())

# title()
print("hello world".title())
print("python programming".title())
print("welcome to uzbekistan".title())

# translate()
table = str.maketrans("aeiou", "12345")
print("hello".translate(table))
print("banana".translate(table))
print("programming".translate(table))

# upper()
print("hello".upper())
print("python".upper())
print("abc123".upper())

# zfill()
print("42".zfill(5))
print("123".zfill(6))
print("hello".zfill(10))


































































































































































































