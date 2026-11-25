pin = int(input("Masukkan PIN 3 digit: "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

# Ekstraksi digit angka
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("\n=== SISTEM KEAMANAN GARASI ===")
print(f"Digit pertama : {digit1}")
print(f"Digit kedua   : {digit2}")
print(f"Digit ketiga  : {digit3}")
print(f"Jam kedatangan: {jam}")

# Logika pengecekan akses
if pin % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status = "Akses Ditolak Sepenuhnya"

# Status CCTV menggunakan ternary operator
cctv = "Mode Malam Merekam" if jam > 18 else "Mode SiangStandby"

# Display Output
print(f"Status Akses : {status}")
print(f"Status CCTV  : {cctv}")
