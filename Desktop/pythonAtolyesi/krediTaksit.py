anapara = float(input("Anapara (TL): "))  # Anapara miktarını al
faiz_orani = float(input("Yıllık Faiz Oranı (%): ")) / 100  # Yıllık faiz oranını al ve yüzdelik formatta kullan
vade = int(input("Vade (ay): "))  # Vade süresini al

# Aylık faiz hesabı
aylik_faiz_orani = faiz_orani / 12  # Aylık faiz oranını hesapla

# Aylık taksit hesabı
aylik_taksit = (anapara * aylik_faiz_orani * (1 + aylik_faiz_orani) ** vade) / ((1 + aylik_faiz_orani) ** vade - 1)

# Toplam geri ödeme miktarı
toplam_geri_odeme = aylik_taksit * vade  # Toplam geri ödemeyi hesapla

# Sonuçları yazdır
print("Aylık taksit: ", round(aylik_taksit, 2), 'TL')
print("Toplam geri ödeme: ", round(toplam_geri_odeme, 2), 'TL')
