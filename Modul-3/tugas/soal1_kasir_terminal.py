# SOAL 1 - Kasir Terminal Bus Sidoarjo (Pak Budi)

jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

print("=== KASIR TERMINAL BUS SIDOARJO ===")
print("Masukkan jarak penumpang (km). Ketik 0 untuk selesai.")

while True:
    jarak = int(input("Jarak penumpang (km): "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak negatif tidak valid, silakan ulangi!")
        continue

    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Penumpang ke-", jumlah_penumpang, "mendapat diskon 50%!")

    print("Tarif: Rp%d" % tarif)

    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("=== REKAP AKHIR ===")
if jumlah_penumpang == 0:
    print("Tidak ada penumpang.")
else:
    rata_rata = total_jarak / jumlah_penumpang
    print("Jumlah penumpang :", jumlah_penumpang)
    print("Total pendapatan : Rp%d" % total_pendapatan)
    print("Jarak terjauh    :", jarak_terjauh, "km")
    print("Rata-rata jarak  : %.2f km" % rata_rata)
