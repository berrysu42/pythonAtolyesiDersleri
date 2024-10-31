#Dosya işlemleri
#Dosya okuma yazma: r, mevcut olan dosyaları okumak için açar.
#Dosya yoksa yeni dosya oluşturma: w, eğer dosya var ise içeriği silip yeni dosya açar.
#Dosya yoksa dosya oluşturur. varsa da imleçten başlayarak dosyaya ekleme yapma: a
# r+ : dosyayı hem okur hem yazar.


#Uygulamalar

"""
file = open("deneme1.txt","w")
file.close()
"""
"""
#with yapısıy kullanarak close komutuna gerek kalmadan dosyamızı otomatik kapatır.
with open("deneme1.txt","w") as file:
    print("Dosya işlemleri")
"""

"""
#dosyaya veri yazmak için 2 fonksiyon kullanırız.
#dosya-nesnesi.write(karakter) #dosyaya karakter dizisi ekler
#dosya-nesnesi.writelines(liste) #dosyaya liste verileri yazar.
with open("deneme1.txt","w") as file:
    file.write("Bir nolu satır bilgileri \n")
    file.write("İki numaralı satır bilgileri \n")
    file.write("Üç numaralı satır bilgileri \n")
    file.write("Dört numaralı satır bilgileri \n")
"""

"""
liste=["aaaaa\n","bbbbb\n","ccccc\n","ddddd\n"]
with open("deneme1.txt","w") as file:
    file.writelines(liste)

with open("deneme2.txt","w") as file:
    for value in liste:
        file.write(value)
"""

"""
#Dosyadan veri okuma
#2 farlı okuma fonksiyonu var. read() ve readline()
#Uygulama
with open("deneme1.txt","w",encoding='utf-8') as file:
    file.write("Bir nolu satır bilgileri \n")
    file.write("İki numaralı satır bilgileri \n")
    file.write("Üç numaralı satır bilgileri \n")
    file.write("Dört numaralı satır bilgileri \n")
    #read fonksiyonuyla dosya içeriğinin tamamını 1 defada okuma
with open("deneme1.txt","r",encoding='utf-8') as file:
        print(file.read())
"""

"""
with open("deneme2.txt","w",encoding='utf-8') as file:
    file.write("Bir nolu satır bilgileri \n")
    file.write("İki numaralı satır bilgileri \n")
    file.write("Üç numaralı satır bilgileri \n")
    file.write("Dört numaralı satır bilgileri \n")
    #readline fonksiyonu ile dosya içeriğini satır satır okuyacağız
with open("deneme2.txt","r",encoding='utf-8') as file:
    while True:
        line=file.readline()
        if not line:
            break
        print(line.split())
print("*************\n")
with open("deneme2.txt","r",encoding='utf-8') as file:
    for line in file:
        print(line.strip())
"""

"""
import os
if os.path .exists("deneme1.txt"):
    os.remove("deneme1.txt")
    print("Dosya Silindi")
else:
    print("Dosya bulunamadı!")
"""
































