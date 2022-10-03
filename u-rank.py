import requests as rt
from bs4 import BeautifulSoup as bf4
bolumismi= input("Bölüm ismi: ")
bo = bolumismi.split()[0]
try:
    bn = bolumismi.split()[1]
except:
    bn=""
if bn == "":
    r = rt.get("https://www.universitego.com/"+bo+"-2020-taban-puanlari-ve-basari-siralamalari/")
else:
    r = rt.get("https://www.universitego.com/"+bo+"-"+bn+"-2020-taban-puanlari-ve-basari-siralamalari/")
soup = bf4(r.content,"html.parser")
q=11
s=6
puanlist=[]
while 1:
    b = soup.find_all("td")[s]
    b = b.text
    a = soup.find_all("td")[q]
    a = a.text
    puanlist.append(b+" : "+a)
    q+=6
    s+=6
    if s == len(soup.find_all("td"))-6:
        break
gelendeger = int(input("sıralama: "))
for i in puanlist:
    try:
        a = i.split()
        if int(a[-1]) >= gelendeger:
            print(i)
    except:
        pass