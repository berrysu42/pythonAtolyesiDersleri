def sum(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Bir sayı sıfıra bölünemez!"
    return x / y

print("Yapmak istediğiniz işlemi seçin: ")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminiz (1/2/3/4): ")
sayi1 = float(input("1. sayı: "))
sayi2 = float(input("2. sayı: "))

if secim == '1':
    print(sayi1, "+", sayi2, "=", sum(sayi1, sayi2))
elif secim == '2':
    print(sayi1, "-", sayi2, "=", subtraction(sayi1, sayi2))
elif secim == '3':
    print(sayi1, "*", sayi2, "=", multiplication(sayi1, sayi2))
elif secim == '4':
    print(sayi1, "/", sayi2, "=", division(sayi1, sayi2))
else:
    print("Geçersiz seçim!")
"""
Benim kod kısmım
def process():
    x = float(input("Birinci sayıyı giriniz: "))
    y = float(input("İkinci sayıyı giriniz: "))
    option =input("Yapmak istediğiniz işlemi seçiniz: '+','-','*','/' ")
    if option == "+":
        result = sum(x, y)
    elif option == '-':
        result = subtraction(x, y)
    elif option == '*':
        result = multiplication(x,y)
    elif option == '/':
        result = division(x,y)
    else:
        print("Hatalı seçim!")
    print("Sonuç: %.2f" % result)

process()
"""