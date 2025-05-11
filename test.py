#liste=[1.2.3.4.5.6.7.8.9]
#for rakam in liste:
  #print(rakam)

#for i in range (10):
  #sonuc *= 2
 #print(i)

#liste1=["a","b","c","d"]
#liste2=[1,2,3,4]
#for harf in liste1:
   #for rakam in liste2:
      #print(harf,rakam)

#liste=[1,2,3,4,5,6,7,8,9]
#for rakam in liste:
    #if rakam == 3:
        #continue
    #print(rakam)
    
    
#liste=[1,2,3,4,5,6,7,8,9]
#for rakam in liste:
    #if rakam == 3:
        #break
    #print(rakam)

#liste=range(100)
#for i in liste:
    #if i% 3 != 0:
       #continue
    #if i == 81:
        #break
    #print(i)

#x=2
#y=3
#while x * y <10000:
    #print(x,y)
    #x += 3 
    #y += 5

#i=1 
#while True:
  #if i %2 == 0:
     #i += 1
     #continue
  #print(i)
  #i += 1
  #if i ==1000:
     #break

#sayi=int(input("Bir sayi giriniz: "))

#faktoriyel = 1
  
  
#for i in range(1, sayi + 1):
  #faktoriyel *= i
#print(f"{sayi}! = {faktoriyel}")

#sayi=int(input("Bir sayi giriniz: "))

#faktoriyel = 1

#i=1

#while i<= sayi:
    #faktoriyel *= i
    #i+=1

#print(f"{sayi}! = {faktoriyel}")


#sayi=int(input("bir sayi giriniz: "))

#prime= True

#for i in range(2,sayi):
   #if sayi%i == 0:
      #prime = False 
      #break
#if prime == True:
 #print(f"{sayi} sayisi asaldir.")
#else:
  #print(f"{sayi} sayisi asal değildir")


#sayi=int(input("bir sayi giriniz: "))

#bolen_sayisi=0
#for i in range(1,sayi+1):
    #if sayi %i== 0:
        #bolen_sayisi+=1
#print(f"{sayi} sayisinin {bolen_sayisi} kadar boleni vardir")


#sayi=int(input("bir sayi giriniz: "))

#str_sayi= str(sayi)
#toplam = 0
#for rakam in str_sayi:
    #toplam += int(rakam)

#print(toplam)

#sayi=int(input("bir sayi giriniz: "))

#toplam = 0
#gecici_sayi = sayi

#while gecici_sayi != 0:
    #basamak = gecici_sayi % 10
    #toplam += basamak
    #gecici_sayi //= 10
#print(toplam)

#liste=[]
#for i in range(5):
    #sayi=int(input("bir sayi giriniz: "))
    #liste.append(sayi)

#print(f"en büyük sayı: {max(liste)}")
#print(f"en küçük sayı: {min(liste)}")

#sayi=int(input("bir sayi giriniz: "))
#karekok = sayi**0.5
#if karekok == int(karekok):
    #print("tamkare")
#else:
    #print("tamkare değil")
                  


#metin=input("bir metin giriniz: ")

#sozluk=dict()

#for harf in metin:
    #if harf in sozluk:
        #sozluk[harf]+=1
    #else:
        #sozluk[harf]=1
#for harf,adet in sozluk.items():
    #print(harf,adet)

#metin=input("bir metin giriniz: ")
#metin2=""

#for harf in metin:
    #if harf == "a":
       #metin2 +="A"
    #else:
        #metin2 +=harf
#print(metin2)


# prime_list=list()
# prime_list.append(2)
# sayi=3
# while True:
#     prime = True
#     for i in range(2,int(sayi ** 0.5+1)):
#         if sayi %i ==0:
#             prime=False
#             break
#     if prime:
#         prime_list.append(sayi)
#         if len(prime_list)==10000:
#             break
#     sayi += 1 
    
# liste2 = []

# for prime in prime_list:
#     strprime = str(prime)
#     if strprime.startswith("3") and strprime.endswith("7"):
#         liste2.append(prime)
# print(len(liste2))


# liste=[]
# for sayi in range(100,1000):
#     toplam = 0
#     gecici_sayi=0
#     while gecici_sayi !=0:
#         basamak = gecici_sayi %10
#         toplam+= basamak **3
#         gecici_sayi //= 10
#     if toplam == sayi:
#        liste.append(sayi)
# print(liste)


# fibonacci_list=[]
# fibonacci_list.append(1)
# fibonacci_list.append(1)

# index = 2
# while True:
#       fibonacci_list.append(fibonacci_list[index-2] + fibonacci_list[index-1])
#       index += 1
#       if len(fibonacci_list) == 100:
#             break
# print(fibonacci_list)


# fibonacci_list=list()
# fibonacci_list.append(1)
# fibonacci_list.append(1)

# index = 2

# while True:
#     fibonacci_list.append(fibonacci_list[index-2] + fibonacci_list[index - 1])
#     terim = fibonacci_list[index-2] + fibonacci_list[index - 1]
#     if len(str(terim)) == 100:
#         print(terim)
#         break
#     index += 1


# def buyukharfecevir(metin):
#     metin = metin.upper()
#     print(metin)
# buyukharfecevir("emir candan")


# def selamla(mesaj,isim = "Anonim"):
#     print(f"{mesaj} {isim}.")

# selamla("Merhaba","Emir")

    
# def indirim_yap(fiyat,yuzde):
#     indirim_miktari = fiyat * (yuzde / 100)
#     indirim_fiyat = fiyat - indirim_miktari
#     print(f"indirimli fiyat: {indirim_fiyat}")

# indirim_yap(100,20)


# def ortalama_hesapla(x,y):
#     return (x+y)/2
# a = ortalama_hesapla(2,6)
# b = ortalama_hesapla(8,10)
# print(a+b)














 

