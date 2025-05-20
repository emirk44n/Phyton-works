f = open("deneme.txt","r")
icerik = f.read()
print(icerik)
f.close()

with open("deneme.txt","r") as f:
    icerik = f.read()
    print(icerik)

with open("deneme.txt","r") as f:
    icerik = f.readlines()
    print(icerik)
    for satir in icerik:
        print(satir)

with open("deneme.txt") as f:
    for satir in f:
        print(satir,end= "")

with open("deneme.txt") as f:
    satir = f.readline()
    print(satir)
    pozisyon = f.tell()
    print(pozisyon)
    f.seek(0)
    satir = f.readline()
    print(satir)

with open("deneme.txt") as f:
    icerik = f.read(10)
    print(icerik,end="")
    icerik = f.read(10)
    print(icerik,end="")
    icerik = f.read(10)
    print(icerik,end="")
    icerik = f.read(10)
    print(icerik,end="")

with open("deneme.txt") as f:
    okunacak_miktar = 10
    icerik = f.read(okunacak_miktar)
    while len(icerik)> 10:
        print(icerik,end="")
        icerik = f.read(okunacak_miktar)

with open("deneme.txt") as okunacak:
    with open("deneme2.txt","w") as yazilacak:
        for satir in okunacak:
            yazilacak.write(satir)

with open("deneme.txt") as okunacak:
    with open("deneme2.txt","w") as yazilacak:
        icerik = okunacak.readlines()
        for satir in okunacak:
            yazilacak.write(satir)

with open("phyton.png","rb") as okuacak:
    with open("phton.png","wb") as yazilacak:
        okunacak_miktar = 1024
        icerik = okunacak.read(okunacak_miktar)
        while len(okunacak_miktar)>0:
            yazilacak.write(icerik)
            icerik = okunacak.read(okunacak_miktar)




