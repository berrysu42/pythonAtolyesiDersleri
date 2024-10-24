"""
import re
txt = "Ankara 'da yağmur yağıyor"
x = re.search(r"^Ankara.*yağıyor$", txt)
if x:
    print("Buldum!")
else:
    print("Bulunamadı!")

txt2 = "Bursa 'da yağmur yağıyor"
x = re.search(r"^Ankara.*yağıyor$", txt2)
if x:
    print("Buldum!")
else:
    print("Bulunamadı!")
"""


"""
findall= Tüm eşleşmeleri göster(liste halinde)
searc=arama yapar ve eşleşme var mı yok mu kontrol eder
split=eşleşme noktalarında böl ve liste oluştur.
"""

"""
import re
txt="Bir gece , Bir gündüz."
x=re.findall("Bir",txt)
print(x)
"""

import re
txt = "Beni anlamadın ya, ben ona yanıyorum."
x = re.split("\s", txt)  # pattern= kısmını kaldırdık
print(x)



























