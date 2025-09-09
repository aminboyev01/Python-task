# #append()
# l=[]
# l.append("cobalt")
# l.append("KOptiva".lower())
# l.append("matiz")
# print(l)
#
#
#
# #clear()
# l.clear()
# print(l)
# l=["salom","alik"]
# l.clear()
# # clear bu royxat set dictni boshatadi faqat elementni
#
#
#
# # copy()
# m=["salom","alik",12]
# l=m.copy()
# print(l)
# s={"salom","wox",19}
# k=s.copy()
# print(k)
# d={"age":19,"ism":"wox"}
# kopya=d.copy()
# print(kopya)
# #yani copy,set,dict,list ga ishlaydi
#
#
#
# #count()
# num=[1,2,3,43,4,56,2,2,3,5]
# print(num.count(3))
# l=["salom","aleykum","nima gap"]
# print(l.count("salom"))
#
# s=("salom",12,243,55,55)
# print(s.count("55"))
#
#
# # extend()
# l=[1,2,3,4,5]
# m=[]
# m.extend(l)
# print(m)
# l=[]
# print(l.extend([1,2,3,4,4,5]))
#
# l.extend({"salom":12,"alik":15})
# print(l)
# # shunda dictda faqat kalitlarni qoshadi  set va tupleni ham qoshsa boladi listga
#
#
# # index()
# l=["cobalt","gentra","matiz"]
# print(l.index("GENTRA".lower()))
#
# #
# # insert()
# # diqqat: insert() metodi faqat listlar (list) uchun mavjud,
# #
# g=[]
# g.insert(0,12)
# print(g)
#
#
#
# # pop()
# # index → ixtiyoriy (berilmasa, oxirgi elementni o‘chiradi).
# # O‘chirgan elementni qaytaradi (return qiladi).
#
# l=[1,23,4,5,7,89,4,"salomat"]
# y=l.pop(3)
# x=l.pop(6)
# print(l)
# print(x)
# print(y)
#
# #
# # remove()
# o=[1,23,4,5,7,89,4,"salomat"]
# o.remove(1)
# o.remove("salomat")
# print(o)
#
#
# # reverse()
# # reverse() – asl ro‘yxatni o‘zgartiradi.
# # [::-1] – yangi nusxa yaratadi, asl ro‘yxat o‘zgarishsiz qoladi.
# l=[1,2,3,4,5,6,7,8,9]
# l.reverse()
# print(l)
# m=l[::-1] # bu yerda listni teskari nusxasi yaratildi
# print(m)
#
#
# #
# # sort()-faqat listda ishlaydi
# sonlar = [4, 2, 9, 1, 7]
# sonlar.sort(reverse=True)
# print(sonlar)
#
# mevalar = ["banan", "olma", "anjir", "gilos"]
# mevalar.sort(key=len)
# print(mevalar)
#
#
# #Metodlar qaysi tipda ishlaydi?
# #
# # List → hammasi ishlaydi (append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort)
# # Tuple → faqat count, index
# # Set → clear, copy, pop, remove
# # Dict → clear, copy, pop
# lis=(1,2,3,4)
# tup=(8,76,5,4)
# ll=lis+tup
# print(ll)













































































#
