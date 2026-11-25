belanja = int(input("Masukan jumlah uang : "))

if belanja % 100000 == 0:
    diskon = 100
    total_bayar = 0
elif belanja % 50000 == 0:
    diskon = 50
    total_bayar = belanja - (belanja * 50 // 100)
elif belanja % 10000 == 0:
    diskon = 20
    total_bayar = belanja - (belanja * 20 // 100)
elif belanja >= 200000:
    diskon = 10
    total_bayar = belanja - (belanja * 10 // 100)
else:
    diskon = 0
    total_bayar = belanja

poin = "Poin Bertambah" if total_bayar > 0 else "Tidak ada poin"

print("uang yang dibawa",belanja)
print("total yang dibayar",total_bayar)
print("mendapat diskon",diskon)
print(poin)