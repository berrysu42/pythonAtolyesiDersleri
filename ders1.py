# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:26:08 2024

@author: berika
"""
"""
name = input("İsminizi giriniz : ")
print("Merhaba",name)
#print(name) 
"""

"""
x="15"
y="39"
print(x+y)
"""
#number1 = float(input("Birinci sayıyı giriniz: "))
#number2 = float(input("İkincinci sayıyı giriniz: "))

#sum = float(number1+number2)
#print(sum)

#diğer yazım
"""
number1 = input("Birinci sayıyı giriniz: ")
number2 = input("İkinci sayıyı giriniz: ")

sum = float(number1)+float(number2)
print(sum)
"""

"""
#karenin alanını bul
kenar = float(input("Kenarı giriniz-> "))
alan = (kenar*kenar)
print("KArenin alanı: ",alan)
"""

"""
exam1 = int(input("1. exam result: "))
exam2 = int(input("2. exam result: "))
exam3 = int(input("3. exam result: "))
average = ((exam1)+(exam2)+(exam3))/3
print("Exam average",average)
"""

"""
vize=input("Vize notu ->")
final=input("Final notu ->")
ort = int(vize)*0.4+int(final)*0.6
print("Ders notu ->",ort)
"""

"""
sayi=int(input("Sayı giriniz -> "))
if(sayi % 2 ==0):
    print("Sayı çiftir.")
else:
    print("Sayı tektir")
"""


"""
num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))
num3 = float(input("Üçüncü sayıyı girin: "))


ortalama = (num1 + num2 + num3) / 3

print("Üç sayının ortalaması:", ortalama)
"""

"""sayının karesi
sayi = 5
karesi=sayi*sayi
print(karesi)
"""

""" kare alan
kenar = 9
alan=kenar* kenar
print(alan)
"""

"""Dikdörtgen alan
kisaKenar=5
uzunKenar=6
cevre=(kisaKenar+uzunKenar)*2
print("Dikdörtgenin çevresi",cevre)
"""

""" üçgen alan
tabanKenar=6
yukseklik=9
alan=(tabanKenar*yukseklik)/2
print("Üçgenin alanı: ",alan)
"""

"""
#daire alan
pi=3
r=15
sonuc=(pi*(r*r))
print(sonuc)
"""

"""
#dongu ornek
tuttugumSayi=23
bilBakalim=int(input("Aklımdan sayı tuttum"))
if bilBakalim==tuttugumSayi:
    print("Tebrikler")
else:
    
    print("Ne yazık ki bilemediniz")
"""

#sayının durumu
"""
sayi = input("sayı girin-> ")
if(int(sayi)<0):
    print(sayi+ " sayısı negetif")
elif(int(sayi)>0):
    print(sayi+ " sayısı pozitif")
else:
    print("Sayı 0'dır")
"""

"""
sayi = input("sayı girin-> ")
if(int(sayi)<0):
    print(sayi+ " sayısı negetif")
if(int(sayi)>0):
    print(sayi+ " sayısı pozitif")
if(int(sayi==0)):
    print("Sayı 0'dır")
"""

#yeniMaas = 0
maas = int(input("Maası giriniz : "))
zam =float( input("Zam oranını giriniz-> "))
yeniMaas = maas +((maas*zam)/100)
print("Zmanlı maas:",yeniMaas)
