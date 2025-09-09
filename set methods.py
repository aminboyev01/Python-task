##  add()
new_set={1,2,3,"olma","anor"}
# new_set.add("meva")
#
# new_set.add(111)
# new_set.add("banan")
# new_set.add("shaptoli")
# print(new_set)

##  clear()
new_set.clear()
f={1,2,4,5,6}
f.clear()
b={"car","toys"}
b.clear()
print(f"{new_set}\n{f}\n{b}")

##  copy()
cop1=new_set.copy()
sett={1,2,4,5,"olma ","anor"}
set1={"q","r","e"}
cop2=sett.copy()
cop3=set1.copy()
print(cop1,cop2,cop3)

# difference()
a={1,2,4,6,7}
b={3,4}
c=a.difference(b)
a1={1,2,3,4,5,6}
b1={4,5,6}
c1=a1.difference(b1)
a2={"olma","anor","anjir"}
b2={"anor"}
d=a2.difference(b2)
print(a,a1,a2)
print(c1,c,d)
## bu asl ro'yxatni ozgartirmaydi nusxa yaratadi
a={1,2,3,4,5,6,7,8}
b={1,2,4,5,6,8}
print(a-b)
##  Yani a-b bilan a.difference(b) ikkalasi bir xil
##   narsa

#########################################
# difference_update()

a1={1,2,3,4,5,6}
b1={4,5,6}
a1.difference_update(b1)
print(a1)
a={1,3,2,4,5,6,7}
b={2,5,3}
a.difference_update(b)
print(a)
# difference_update() asl ro'yxatni o'zgartiradi

##Shunda defference() bn difference_update farqi  difference qiymat qaytaradi
##diffrence_update esa asl royxatni ozgartiradi
#############################################
# discard()
a={1,2,3,4,5,6,7}
a.discard(3)
print(a)

b={1,2,3}
b.discard(3)
print(b)

a={"olma","anor"}
a.discard("olma1")
print(a)
# Agar element mavjud bo‘lsa → olib tashlaydi.
# Agar element mavjud bo‘lmasa → xato bermaydi, jim o‘tib ketadi.
###################################
# remove()
a={12,3,5,6,7}
a.remove(12)
print(a)

v={1,2,3,4,5}
v.remove(12)
print(v)

a={1,2,3,4}
a.remove(4)
print(a)

##Yani discard() bn remove() vazifasi bir lekin remove() da
##error qaytaradi discard() da esa toplamni ozini

######################################
# intersection()
a={1,2,3,5}
b={3,4,5}
d=a.intersection(b)
print(d)  #{3,5}

a={1,2,3,5}
b={3,4,5}
c={1,2,3}
f=a.intersection(b,c)
print(f)

a={1,2,3,5}
b={3,4,5}
c=a&b
print(c)

# Shunda & = intersection()
# intersection()-qiymat qaytaradi asl  setni ozgartirmaydi

#############################################33
# intersection_update()
a={1,2,3,5}
b={3,4,5}
a.intersection_update(b)
print(a)  #{3,5}
print(b)   # {3,4,5}
# bu faqat asl ni ozgartiradi yani ani b ozgarmaydi
# &= bilan qisqa yoziladi
################################################3333
# isdisjoint()
##Bu metod ikki setda umumiy element bormi yo‘qmi shuni tekshiradi.
##Agar umumiy element bo‘lmasa → True
##Agar umumiy element bo‘lsa → False
a={1,2,3}
b={3,4,5}
print(a.isdisjoint(b)) #False

a1={1,2,3,5}
b1={7,8,9}
d=a1.isdisjoint(b1)
print(d)  #True

a2={"olma","anor"}
b2={"meva"}
d1=a2.isdisjoint(b2)
print(d1) #True

# issubset()
# issubset() → kichik set kattasining ichida to‘liq joylashganini tekshiradi.
# <= → kichik yoki teng bo‘lishi mumkin.
# < → faqat kichik bo‘lishi kerak.
a={1,2}
b={1,2,3,4}
d=a.issubset(b)
print(d)
a1={1,2,34566,5,7,7,8}
b1={6,7,8,9}
d1=b1.issubset(a1)
print(d1)
a2={3,4,5,6}
b2={3}
d2=b2.issubset(a2)
print(d2)


# issuperset()
a={1,2}
b={1,2,3,4}
d=b.issuperset(a)
print(d)
a1={1,2,34566,5,7,7,8}
b1={6,7,8,9}
d1=a1.issuperset(b1)
print(d1)
a2={3,4,5,6}
b2={3}
d2=a2.issuperset(b2)
print(d2)


# symmetric_difference()

##Bu metod ikkita setdagi faqat umumiy bo‘lmagan elementlarni qaytaradi.
##O‘xshash (umumiy) elementlar tashlab yuboriladi.
##Faqat farqli elementlar qoladi.

a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)                      # {1, 2, 4, 5}

a1={1,2,3}
b1={3,4,5,6}
print(a1.symmetric_difference(b1))

a2={"olma","anjir","kompot"}
b2={"kampot"}
d2=a2.symmetric_difference(b2)
print(d2)
#asl setni ozgartirmaydi natijani copy qilad

#  union()

# union() → yangi set qaytaradi, asl setlar o‘zgarmaydi. setlarni birlashtirad
# | operatori → qisqa yo‘li.
a={1,2}
b={3,4}
c=a.union(b)
print(c) # copy yaratadi

a1={1,2,4,5}
b1={4,5,6,7,8}
c1={8,9}
d2=a1.union(b1,c1)
print(d2)

# update()

# Bu metod union() ga o‘xshaydi, lekin farqi shundaki:
# update() → asl setni o‘zgartiradi (natijani o‘ziga yuklaydi).
# union() → yangi set qaytaradi, asl setlar o‘zgarmaydi.
a={1,2,3,5}
b={4,6,7}
a.update(b)
print(a)

a1={2,3,5,6}
b1={7,8,9}
a1.update(b1)
print(a1)
a2={"olma"}
b2={"anjir"}
a2.update(b2)
print(a2)





















