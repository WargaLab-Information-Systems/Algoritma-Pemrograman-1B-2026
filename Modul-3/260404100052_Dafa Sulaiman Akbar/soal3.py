jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

total = 0
tertinggi = -1
terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print("\nMahasiswa ke-", i)
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        kategori = "A"
        jumlah_a += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_b += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1

    print("--- Hasil ---")
    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", round(akhir, 2))
    print("Kategori    :", kategori)

    total += akhir
    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("\n=== REKAP KELAS ===")
print("Jumlah nilai A :", jumlah_a)
print("Jumlah nilai B :", jumlah_b)
print("Jumlah nilai C :", jumlah_c)
print("Jumlah nilai D :", jumlah_d)
print("Jumlah nilai E :", jumlah_e)
print("Nilai tertinggi :", round(tertinggi, 2), "atas nama", nama_tertinggi)
print("Nilai terendah  :", round(terendah, 2), "atas nama", nama_terendah)
print("Rata-rata nilai :", round(total / 10, 2))