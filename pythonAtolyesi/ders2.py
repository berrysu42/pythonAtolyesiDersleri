#Loops
"""
range(başlangıçDeğeri,bitişDeğeri,adim)
for i in range(1,15,3) 1'den 15'e kadar 3'er 3'er ilerle
"""

"""
while döngüsü bir şarta bağlanır.
sayac=1
while sayac>1: gibi
"""
"""
for i in range(1,6):
    print(i)
"""

"""
sayilar = [1,2,3,4,5]
sum = 0
for sayi in sayilar:
    sum+=sayi
print("Toplam...->",sum)
"""

"""
word = "Merhaba"
for letter in reversed(word):
    print(letter)
"""

"""asal sayı kontrolü
counter = 0
sayi = int(input("Sayı gir...-> "))

# Asal sayı kontrolü yap
for i in range(2, sayi):
    if sayi % i == 0:  # Sayının kendisinden ve 1'den başka böleni varsa
        counter += 1  # Sayı asal değil, counter artırılır
        break  # Döngüden çıkılır, çünkü asal olmadığı anlaşılmıştır

# Sonuç kontrolü
if counter != 0:
    print("Sayı asal değildir.")
else:
    print("Sayı asaldır.")
"""
"""
i=1
while i<5:
    print(i)
    i+=1
"""

"""
#tek mi cift mi
x=1
while x <= 100:
    if(x%2 ==0):
        print(f"{x} sayısı çifttir.")

    else:
        print(f"{x} sayısı tektir.")

    x+=1
print("Tamamlandı")
"""

"""
x=0
result = 0
while x <= 100:
    x+=1
    if x % 2 == 0:
        continue
    result+=x
print(f'toplam: {result}')
"""

"""
urunler = []
adet = int(input("Kaç adet ürün eklemek istiyorsunuz?..->"))
i=0
while(i<adet):
    name=input("Ürün ismi: ")
    price=input("Ürün fiyati: ")
    urunler.append({
        "name":name,
        "price":price
    })
    i+=1
for urun in urunler:
    print(f'urun adı: {urun["name"]} ürün fiyatı {urun["price"]}')
"""


#FONKSİYONLAR
"""
def hello():
    print("MErhaba")
hello() #fonksiyon çağırma
"""
"""
#fonksiyonlara parametre gönderme
def hello(name):
    print("Merhaba "+name)
hello("Berika")
"""

"""
def sum(a,b):
    return a+b
sonuc=sum(102,15)
print(sonuc)
"""

"""
#cift sayıları döndüren fonksiyon
def is_even(x):
    return x%2==0
def listFilter(filterFonction,myList):
    return [x for x in myList if filterFonction(x)]
numbers = [1,2,3,4,5,6]
evenNumbers = listFilter(is_even,numbers)
print(evenNumbers)
"""

"""
#fibonacci
def fibonacci (n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(10))
"""

"""
#cümle sayısını bulma
def wordcount(sentence):
    words=sentence.split()
    return len(words)
print(wordcount("Merhaba Tech."))
"""

"""
#faktoriyel
def faktoriyel(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * faktoriyel(n-1) #recursive durum
print(faktoriyel(5))
"""


"""
#KDV hesaplama
def kdv_account(price):
    return price*0.18
def sum_price(price):
    return price + kdv_account(price)

#print(kdv_account(50))
#print(sum_price(50))

price=125
total_price = sum_price(price)
print(total_price)
"""

"""
#indirim hesabı
def calculate_percentage(price,percentage):
    return (price*percentage)/100


def discount_price_calculate(price,discount_percentage):
    discount=calculate_percentage(price,discount_percentage)
    return price-discount

price=200
discount_percentage=10
discount_price = discount_price_calculate(price,discount_percentage)
print(discount_price)
"""

"""
#daha kısa yol olan hesaplama
def calculate_discounted_price(price, discount_percentage):
    return price * (1 - discount_percentage / 100)

price = 200
discount_percentage = 10
discount_price = calculate_discounted_price(price, discount_percentage)
print(discount_price)  # 180.0
"""

"""
def back(num):
    if num <= 0:
        print("Zero!")
        return
    else:
        smileFace = []
        for i in range(0,num):
            smileFace+= "🤞" #smileFace.append("🤞")
        print(num," ".join(smileFace))
        back(num-2)
back(9)
"""

def cift_mi(x):
    return x % 2 ==0
sum=0
counter = 0
start = int(input("Başlangıç sayısı ne? ..->"))
finish = int(input("Başlangıç sayısı ne? ..->"))

for sayi in range(start,finish+1):
    if(cift_mi(sayi)):
        sum = sum+sayi
        counter+=1
print("Toplam-> ",sum)
print('Ortalama',float(sum/counter))