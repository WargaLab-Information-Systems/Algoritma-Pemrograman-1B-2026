jumlah_penumpang = 0
total = 0
total_jarak = 0
terjauh = 0

while True:
    jarak = float(input("Masukkan jarak penumpang (km), dan 0 untuk selesai: "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, ulangi!")
        continue

    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah_penumpang % 5 == 0:
        tarif *= 0.5

    total += tarif
    total_jarak += jarak
    terjauh = max(terjauh, jarak)

rata = total_jarak / jumlah_penumpang if jumlah_penumpang > 0 else 0

print("Jumlah penumpang :", jumlah_penumpang)
print("Total pendapatan : Rp", total)
print("Jarak terjauh    :", terjauh, "km")
print("Rata-rata jarak  :", round(rata, 1), "km")