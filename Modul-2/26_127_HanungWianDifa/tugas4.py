# Program Akses Garasi Jendral Wito

pin = int(input("Masukkan PIN 3 digit: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

# Memisahkan digit PIN
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("\nDigit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)

# Menentukan akses pintu
if pin % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka"
        
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"
        
else:
    status = "Akses Ditolak Sepenuhnya"

print("Status Akses  :", status)

# Ternary operator untuk CCTV
status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
print("Status CCTV   :", status_cctv)