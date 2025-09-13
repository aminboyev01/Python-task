##1
# def user_date(firs_name,last_name,age):
#     name=f"ismi: {firs_name}"
#     lastname=f"Familiya: {last_name}"
#     ag=f"yoshi: {age}"
#     print(f"{name}\n{lastname}\n{ag}")
# firs_name=input("Ismingizni kiriting: ").title()
# last_name=input("Familiyangizni kiriting: ").title()
# age=input("Yoshingizni kiriting: ").title()
# user_date(firs_name,last_name,age)



##2
# def find_max(a,b,c):
#     max_value=max(a,b,c)
#     result=[]
#     if a==max_value:
#         result.append("A")
#     if b==max_value:
#         result.append("B")
#     if c==max_value:
#         result.append("C")
#     print(f"Eng katta son => {' va '.join(result) } = {max_value}")
# a=int(input("a ni kiriting: "))
# b=int(input("b ni kiriting: "))
# c=int(input("c ni kiriting: "))
#
# find_max(a,b,c)

##3

# def find_word(word,letter):
#     find_let=word.count(letter)
#     print(f"{word} so'zida {letter} belgisi\n{find_let}-marta qatnashgan")
# word=input("so'z kiriting: ")
# letter=input("Belgi kiriting: ")
# find_word(word,letter)

##4

# def list_sum(my_list):
#     print(f"List raqamlar yig'indisi: {sum(my_list)} ")
# my_list = list(map(int, input("Sonlarni probel bilan kiriting: ").split()))
# list_sum(my_list)
##5
# def daraja(a,b):
#     '''Daraja hisoblovchi dastur '''
#     d=a**b
#     print(f"a ni b darajasi: {d} ")
# daraja(3,2)

##6
# def daraja3(a,b,c,d):
#     ab=a**b
#     ac=a**c
#     ad=a**d
#     print(f"a ning b chi darajasi: {ab}\na ning c chi darajasi: {ac}\na ning d chi darajasi: {ad}")
# daraja3(2,3,4,5)
#

##7
# def digit_count_sum(word):
#     '''Matndagi raqamlarni sanash va yig'indisini hisoblash dasturi'''
#     total=0
#     count=0
#     for i in word:
#         if i.isdigit():
#             count+=1
#             total+=int(i)
#
#     print(f"Raqamlar soni wordagi: {count}")
#     print(f"Raqamlar yig'indisi: {total}")
#
# digit_count_sum('dsfhsiruf123')

##8
# def add_right(a,b):
#     result=int(str(a)+str(b))
#     print(f"Natija: {result}")
# add_right(12,34)
#

##9
# def add_left(a,b):
#     result=int(str(b)+str(a))
#     print(f"Natija: {result}")
# add_left(12,34)

##10
# def work_with_list(a):
#     '''bu funksiya a listdan eng kichik sonni
#     topib list elementlariga ko'paytirib
#     qiymatini o'zgartiradi va listni print qilsin.'''
#     min_val=min(a)
#     m=[]
#     for num in a:
#         l=num*min_val
#         m.append(l)
#     print(m)
# a=list(map(int,input("sonlarni probel bilan kiriting: ").split()))
# work_with_list(a)

##11

# def big_sales(sales):
#     '''Qaysi oyda narsa kop sotilganini hisoblovchi dastur'''
#     max_val=max(sales.values())
#     for key,value in sales.items():
#         if value==max_val:
#             return key
#             break
# sales={
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
#     }
# print(big_sales(sales))
##12
# def min_max(numbers,min_num,max_num):
#     '''Numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlash'''
#     min_val=min(numbers)
#     max_val=max(numbers)
#     if min_val==min_num:
#         print(f"Listdagi {min_num} kichik son!\n")
#     else:
#         print(f"Kichiki emas {min_num}\n")
#
#     if max_val==max_num:
#         print(f"Listdagi kattasi {max_num}!")
#     else:
#         print(f"{max_num} kattasi  emas")
#
# numbers=[2,3,4,5,7,8,9]
# min_max(numbers,2,8)
##13
#
# def expensiveProduct(products):
#     lis=[]
#     for product in products:
#         lis.append(product['price'])
#     max_p=max(lis)
#     for product in products:
#         if product['price']==max_p:
#             print(f"Eng qimmat telefon: {product['name']}")
#
#
#
#
# products= [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ]
#
# expensiveProduct(products)
















