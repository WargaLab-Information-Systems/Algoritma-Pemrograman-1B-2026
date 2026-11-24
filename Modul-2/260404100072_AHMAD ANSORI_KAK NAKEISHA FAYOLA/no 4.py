# Input PIN dan jam kedatangan
pin = int(input("Masukkan 3 digit PIN: "))
jam = int(input("Masukkan jam kedatangan : "))

# Memisahkan 3 digit PIN secara matematis
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

print("\n=== HASIL PEMISAHAN PIN ===")
print("Digit pertama :", digit1)
print("Digit kedua   :", digit2)
print("Digit ketiga  :", digit3)

# Menentukan status akses garasi
if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Dinyalakan")

elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")

else:
    print("Akses Ditolak Sepenuhnya")

# Ternary operator untuk status CCTV
status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang"

print("Status CCTV:", status_cctv)