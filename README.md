# SHADOWUNYER-
def topla(x, y):
    """İki sayıyı toplar"""
    return x + y

def cikar(x, y):
    """İki sayıyı çıkarır"""
    return x - y

def carp(x, y):
    """İki sayıyı çarpar"""
    return x * y

def bol(x, y):
    """İki sayıyı böler. Sıfıra bölme hatasını kontrol eder."""
    if y == 0:
        return "Hata! Sıfıra bölme yapılamaz."
    return x / y

print("Yapmak istediğiniz işlemi seçin:")
print("1. Toplama (+)")
print("2. Çıkarma (-)")
print("3. Çarpma (*)")
print("4. Bölme (/)")

while True:
    # Kullanıcıdan işlem seçimi alınır
    secim = input("Seçiminizi girin (1/2/3/4): ")

    # Seçimin geçerli olup olmadığını kontrol et
    if secim in ('1', '2', '3', '4'):
        try:
            sayi1 = float(input("İlk sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Geçersiz giriş. Lütfen sayı girin.")
            continue # Döngünün başına dön

        if secim == '1':
            print(f"{sayi1} + {sayi2} = {topla(sayi1, sayi2)}")

        elif secim == '2':
            print(f"{sayi1} - {sayi2} = {cikar(sayi1, sayi2)}")

        elif secim == '3':
            print(f"{sayi1} * {sayi2} = {carp(sayi1, sayi2)}")

        elif secim == '4':
            sonuc = bol(sayi1, sayi2)
            print(f"{sayi1} / {sayi2} = {sonuc}")
            
        # Başka bir işlem yapıp yapmak istemediğini sor
        yeni_hesap = input("Başka bir hesaplama yapmak ister misiniz? (e/h): ")
        if yeni_hesap.lower() == "h":
            break

    else:
        print("Geçersiz Giriş")
