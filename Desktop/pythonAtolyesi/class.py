"""
içerisinde değişken ve fonksiyon barındıran ve yeri geldiğinde bunları bize taslak
döndüren yapılardır.
"""

"""
class Sinifim:
    x=5
ogr1=Sinifim()
print(ogr1.x)
"""
#__init__() fpnksiyonu
"""
class ogr:
    name=None
    age=None
    class_is=None
    discontinuity=None
"""

"""
class Ogr:
    name = "-"
    age = 15

    def selamVer(self):
        print("Merhaba")

# Sınıfın bir örneğini oluştur
ogrenci = Ogr()

# Sınıfın özelliklerine ve metotlarına örnek üzerinden eriş
print(ogrenci.name)
print(ogrenci.age)
ogrenci.selamVer()
"""

"""
class Kisi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Kisi("Ayşe",25)
print(p1.name)
print(p1.age)
"""


"""
class Kisi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def yazdir(self):
        print("Merhaba,adım",self.name,"yaşım da",self.age,"'dır")
p1=Kisi("Murat",36)
p1.yazdir()
"""


"""
class sinifKitap:
    group="Kitap"
    #sınıf dışından erişilemeyen değişken bildirimleri(çift_ile (__) başlar)
    __author=''
    def __init__(self,category,name,author_name):
        self.category=category
        self.name=name
        self.__author=author_name
    def writeObject(self):
        print(self.group+ ':'+ self.category+ '->'+
              self.name+'->'+self.__author)

obj1=sinifKitap('Roman','Çalıkuşu','Reşat Nuri Güntekin')
obj1.writeObject()

obj2=sinifKitap('Hikaye','ÇPerili Köşk','Ömer Seyfettin')
obj2.writeObject()
"""

"""
class Bike:
    name=""
    gear=""
bike1=Bike()
bike1.gear=11
bike1.name="Zirve Bisiklet"
print(f"Name: {bike1.name},Gears:{bike1.gear}")
"""

class Room:
    length=0.0
    breadth=0.0

    def calculate_area(self):
        print("Area of Room = ",self.length*self.breadth)
study_room = Room()
study_room.length=42.5
study_room.breadth=30.5
study_room.calculate_area()