# import sqlite3
#
# # 1. Baza bilan ulanish
# conn = sqlite3.connect("students.db")
# cursor = conn.cursor()
#
# # 2. Agar jadval bo'lmasa, uni yaratamiz
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     grade TEXT
# )
# """)
#
# # 3. Jadvalga yangi ma'lumot qo'shamiz
# cursor.execute("""
# INSERT INTO students (name, age, grade)
# VALUES ('Shohrux', 18, 'A')
# """)
#
# # 4. O'zgarishlarni saqlaymiz
# conn.commit()
#
# print("Baza yaratildi va ma'lumot qo'shildi!")
#
# # 5. Bog'lanishni yopamiz
# conn.close()




import sqlite3

# 1. Baza bilan ulanish
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# 2. Agar jadval bo'lmasa, yaratamiz
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")

# 3. Bir nechta talaba qo'shamiz
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Ali', 20, 'B')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Laylo', 19, 'A')")
cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Jasur', 21, 'C')")

# O'zgarishlarni saqlaymiz
conn.commit()

# 4. Barcha talabalarni chiqaramiz
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Talabalar ro'yxati:")
for row in rows:
    print(row)

# 5. Bog'lanishni yopamiz
conn.close()




























































































































