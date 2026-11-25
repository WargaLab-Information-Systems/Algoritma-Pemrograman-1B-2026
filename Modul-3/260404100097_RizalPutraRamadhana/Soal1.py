penumpang = 0
total_harga = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = int(input("masukkan jarak (0 untuk selesai): "))

    if jarak == 0:
        break
    penumpang += 1
    total_jarak += jarak

    print("penumpang ke = ", penumpang)

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
    
    if jarak < 0 :
        print("tidak dihitung")
        penumpang -= 1
    elif jarak <= 5:
        harga = 3000
        print(harga)
    elif jarak > 5 and jarak <= 15:
        selisih = jarak - 5
        harga = 3000 + (selisih * 1000)
        print(harga)
    else:
        selisih = jarak - 15
        harga = 13000 + (selisih * 500)
        print(harga)

    if penumpang % 5 == 0:
        diskon = harga * 0.50
        total_harga = harga - diskon
        print("mendapatkan diskon 50% = ", diskon)
        print("harga setelah diskon = ", total_harga)

    total_harga += harga

print("total penumpang = ", penumpang)
print("total harga keseluruhan = ", total_harga)
print("jarak terjauh = ", jarak_terjauh)
print("rata rata jarak = ", total_jarak / penumpang)