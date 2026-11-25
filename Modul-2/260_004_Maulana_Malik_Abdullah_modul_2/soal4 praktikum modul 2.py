# input
pin = int(input("Masukkan 3 digit kode PIN: "))
jam = int(input("Masukkan jam kedatangan anda: "))

# pemisahan digit secara sistematis
d1 = pin // 100
d2 = (pin // 10) % 10
d3 = pin % 10

print("Digit pertama :", d1)
print("Digit kedua :", d2)
print("Digit ketiga :", d3)

# status akses pintu garasi
if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Menghidupkan Lampu")
elif pin % 2 == 0:
    if d1 + d3 == d2:
        print("Garasi VIP Terbuka Untuk Boss")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi, ADA PENYUSUP!")
else:
    print("Akses Ditolak")

#status CCTV dengan ternary operator
status_cctv = "Mode Malam Marekam" if jam > 18 else "Mode Siang Standby"
print(status_cctv)    