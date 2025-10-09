import  requests
from bs4 import BeautifulSoup

##sayt manzil
url="https://daryo.uz"
respons=requests.get(url)
print(respons.status_code)
##sahifa sarlavhasini olamz
soup=BeautifulSoup(respons.text,"html.parser")
title=soup.title.text
print(f"Title:{title}")
## barcha h3 teglarini olamz
h1_format=soup.find_all("h3")
print("h3 formatdagi so‘zlar:")
for tag in h1_format:
    print(tag.text.strip())

## barcha p teglari
p_format=soup.find_all("p")
print("p formatdagi sozlar: ")
for tag in p_format:
    print(tag.text.strip())

#Barcha a teglari(matni)
print(f"Barcha linklar:\n")
print("link:")
print("link:")
print("link:")
print("link:")

link=soup.find_all("a")
for tag in link:
    print(tag.text.strip())

## Barcha a teglar havolasi
print("Havolalar: ")
print("Havolalar: ")
print("Havolalar: ")
print("Havolalar: ")
for tag in soup.find_all("a", href=True):
    print(tag["href"])












