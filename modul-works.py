# import random
# from datetime import date
# import time
# from datetime import timedelta

# for i in range(10):
#     print(random.random())

# for i in range(10):
#     print(random.uniform(10,30))

# for i in range(10):
#     print(random.randint(1,10))

# for i in range(10):
#     print(random.randrange(1,10,2))

# liste = ["Siyah","Mavi","Yeşil","Gri","Turuncu","Pembe"]
# random.shuffle(liste)

# print(random.choice(liste))

# print(random.sample(liste,2))

# zarlar = {1: 0,2: 0,3: 0 ,4: 0,5: 0,6: 0}

# for i in range(100):
#     zar = random.randint(1, 6)
#     zarlar[zar] += 1 

# for zar in zarlar:
#     print(f"{zar} gelme olasiliği: {zarlar[zar] / 100}") 

# alti_alti = 0
# deneme_sayisi = 0
# while True:
#       deneme_sayisi += 1
#       zar1 = random.randint(1,6)
#       zar2 = random.randint(1,6)
#       if zar1 == 6 and zar2 == 6:
#          alti_alti += 1
#       if alti_alti == 10:
#           print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} defa atildi.")
#           break  
    


# baslangic = time.time()
# liste = []
# for i in range(1000000):
#     liste.append(i)
# bitis = time.time()
# print(bitis-baslangic)

# zaman =time.ctime()
# print(zaman)

# zaman =time.localtime()
# print(zaman)

# zaman2 =time.localtime()
# zaman =time.asctime(zaman2)
# print(zaman)


# zaman = time.strftime("%d.%m.%Y %H:%M:%S")
# print(zaman)

# print("Program başladi.")
# time.sleep(3)
# print("Program sonlandi.")


# bugun = date.today()
# print(bugun)

# gecmis_tarih=date(2015,7,15)
# print(gecmis_tarih)

# gecen_zaman = bugun - gecmis_tarih
# print(gecen_zaman)


# suan = datetime.now()
# print(suan)
# print(suan.year)
# print(suan.month)
# print(suan.day)
# print(suan.hour)
# print(suan.minute)
# print(suan.hour)
# print(suan.second)
# print(suan.microsecond)

# gecmis_an = datetime(2015,7,15,4,1,31,313)
# print(suan-gecmis_an)


# suan = datetime.now()
# tdelta = timedelta(days=7,hours=5,second=69)
# print(suan + tdelta)
# print(suan - tdelta)


# pazar_sayisi = 0
# for yil in range(1980,2001):
#     for ay in range(1,13):
#         if datetime(yil,ay, 1).weekday()==6:
#             pazar_sayisi += 1
# print(pazar_sayisi)


import os 

# print(os.getcwd())
# os.chdir("C:\Users\90542\Desktop\repos")
# print(os.listdir(C:\Users\90542\Desktop\repos))
for dosya in os.listdir():
    print(dosya)
os.mkdir("deneme")
os.makedirs("deneme1/deneme2")
os.rmdir("deneme")
os.removedirs("deneme1/deneme2")


os.chdir("C:\Users\90542\Desktop\repos")
silinecek = os.listdir()[0]
os.remove(silinecek)
os.rename("deneme.docx","Deneme.docx")

print(os.stat("Deneme.docx").st_atime)
zaman = datetime.fromtimestamp(os.stat("Deneme.docx").st_atime)
print(zaman)

print(os.stat("Deneme.docx").st_size)
print(os.stat("Deneme.docx").st_mtime)


os.chdir("C:\Users\90542\Desktop\repos")

for gecerli_klasor, icindeki_klasor, icindeki_dosyalar in os.walk("C:\Users\90542\Desktop\repos"):
    print("Gecerli klasor: " ,gecerli_klasor)
    print("Icindeki klasor: " ,icindeki_klasor)
    print("Icindeki dosyalar: " ,icindeki_dosyalar)
    print()


os.chdir("C:\Users\90542\Desktop\repos")
print(os.path.join("deneme1","deneme2","deneme3"))

print(os.path.isfile("C:\Users\90542\Desktop\repos"))
print(os.path.isdir("C:\Users\90542\Desktop\repos"))
print(os.path.splitext("C:\Users\90542\Desktop\repos"))



