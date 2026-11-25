pin = int(input("Masukan 3 digit pin: "))
jam = int(input("masukan jam kedatangan (0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        akses = "garasi pagi terbuka"
    else:
        akses = "garasi malam terbuka"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        akses = "Garasi VIP Terbuka Khusus Bos"
    else:
        akses = "kode genap ditolak, alarm berbunyi"
else:
    akses = "akses ditolak"

cctv = "Mode malam merekam" if jam > 18 else "mode siang standby"

print("digit pertama :",digit1)
print("digit kedua :",digit2)
print("digit ketiga :",digit3)
print("status akses: ",akses)
print("status cctv: ",cctv)
