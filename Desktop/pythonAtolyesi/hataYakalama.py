#try, except, finally
"""
try:
    print(x)
except:
    print("Bir hata oluştu!")

try:
    print(x)
except NameError:
    print("x tanımlanmamış!")
except:
    print("Başka bir hata meydana geldi!")
"""

try:
    sayi = int(input("Yaşı giriniz..-> "))
    if sayi < 18:
        print("Sisteme giriş için 18 üzeri olman gerekir!")
except (ValueError,ZeroDivisionError):
    print("Bu alana sadece rakam girebilirsiniz!")
except Exception as e:
    print(f"Tanımsız bir hata oluştu: {e}")
