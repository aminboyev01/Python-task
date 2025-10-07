import re
##1
emails = [
    "ali@gmail.com",
    "test.user@yahoo.uz",
    "invalid@",
    "@example.com",
    "user@domain"
]

pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

for email in emails:
    if re.match(pattern, email):
        print(f"{email} → To'g'ri email")
    else:
        print(f"{email} → Noto'g'ri email")

###################################################
##2

# text = """
# Aloqa: +998901234567
# Raqam: 998971234567
# Tel: 901234567 (noto'g'ri)
# """
#
# pattern = r'(?:\+?998)?(\d{9})'
#
# matches = re.findall(pattern, text)
#
# for number in matches:
#     formatted = f"+998 {number[:2]} {number[2:5]} {number[5:7]} {number[7:]}"
#     print(f"Topildi: {formatted}")
#
#
