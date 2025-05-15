import os

def duzenle():
    klasor = input("Düzenlenecek klasor: ")
    dosyalar = [] #dosyalar depolanacak
    uzantilar = [] #uzantılar depolanacak
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)): #dosyamız bir klasor mu onun kontrolu
                continue
            if dosya.startswith("."): #dosyamız gizli bir dosya mı onun kontrolu
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    #uzantıları alma
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        if uzanti in uzantilar:
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantilar:
        if os.path.isdir(os.path.join(klasor.uzanti)):
            continue
        else: 
            os.mkdir(os.path.join(klasor,uzanti))
    uzanti = dosya.split(".")[-1]
    os.rename(os.path.join(klasor,uzanti),os.path.join(klasor,uzanti,dosya))

if __name__ == "__main__":
    duzenle()