jumlah = 0
total = 0
terjauh = 0
total_jarak = 0

print("<KASIR TERMINAL BUS SIDOARJO>")
print("Masukkan 0 untuk berhenti")

while True:
    jarak = int(input("Jarak penumpang (km): "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid, ulangi!")
        continue

    jumlah += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah % 5 == 0:
        tarif = tarif // 2
        print("Penumpang ke-", jumlah, "dapat diskon 50%")

    print("Tarif: Rp", tarif)

    total += tarif
    total_jarak += jarak
    if jarak > terjauh:
        terjauh = jarak

print("\n=== REKAP ===")
print("Jumlah penumpang :", jumlah)
print("Total pendapatan : Rp", total)
if jumlah > 0:
    print("Jarak terjauh    :", terjauh, "km")
    print("Rata-rata jarak  :", (total_jarak // jumlah), "km")