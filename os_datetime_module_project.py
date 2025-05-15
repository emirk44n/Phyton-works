import os
from datetime import datetime

def duzenle():
    klasor = input("Düzenlenecek klasor: ")
    dosyalar = [] #dosyalar depolanacak
    tarihler = [] #tarihler depolanacak
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)): #dosyamız bir klasor mu onun kontrolu
                continue
            if dosya.startswith("."): #dosyamız gizli bir dosya mı onun kontrolu
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    #tarihleri alma
    for dosya in dosyalar:
        tarih_damgasi = os.stat(os.path.join(klasor,dosya)).st_birthtime
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d.%m.%Y")
        if tarih in tarihler:
            continue
        else:
            tarihler.append(tarih)  

    for tarih in tarihler:
        if os.path.isdir(os.path.join(klasor.tarih)):
            continue
        else: 
            os.mkdir(os.path.join(klasor,tarih)) 
    tarih_damgasi = os.stat(os.path.join(klasor,dosya)).st_birthtime
    tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d.%m.%Y")
   
    os.rename(os.path.join(klasor,tarih),os.path.join(klasor,tarih,dosya))

if __name__ == "__main__":
    duzenle()