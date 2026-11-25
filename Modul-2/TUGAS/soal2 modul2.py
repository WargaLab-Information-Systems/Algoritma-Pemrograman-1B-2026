print("===========================================")
totbelanja = int(input("Masukkan jumlah total belanja: "))

print("-------------------------------------------")
if totbelanja % 100000 == 0:
    print("Diskon 100%/Gratis", "harga yang harus dibayar Rp.", totbelanja-totbelanja*100/100)
elif totbelanja % 50000 == 0:
    print("Diskon 50% ", "harga yang harus dibayar Rp.", totbelanja-totbelanja*50/100)
elif totbelanja % 10000 == 0:
    print("Diskon 20% ", "harga yang harus dibayar Rp.", totbelanja-totbelanja*20/100)
elif totbelanja >=200000:
    print("Diskon 10% ", "harga yang harus dibayar Rp.", totbelanja-totbelanja*10/100)
else:
    print("kasian ga dapet diskon...", "harga yang harus dibayar Rp.", totbelanja)
print("-------------------------------------------")
print("><poin bertambah><") if totbelanja > 0 else print("><tidak ada poin><")
print("===========================================")