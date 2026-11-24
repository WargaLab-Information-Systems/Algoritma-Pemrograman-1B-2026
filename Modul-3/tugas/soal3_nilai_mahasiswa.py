# SOAL 3 - Pengelolaan Nilai 10 Mahasiswa

jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

total_nilai_akhir = 0
tertinggi = -1
terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print("--- Data mahasiswa ke-%d ---" % i)
    nama = input("Nama        : ")
    tugas = float(input("Nilai tugas : "))
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

    print("HASIL:", nama)
    print("  Tugas: %.1f | UTS: %.1f | UAS: %.1f" % (tugas, uts, uas))
    print("  Nilai akhir: %.2f | Kategori: %s" % (akhir, kategori))
    print()

    total_nilai_akhir += akhir

    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("=== REKAP KELAS ===")
print("Jumlah nilai A:", jumlah_a)
print("Jumlah nilai B:", jumlah_b)
print("Jumlah nilai C:", jumlah_c)
print("Jumlah nilai D:", jumlah_d)
print("Jumlah nilai E:", jumlah_e)
print("Nilai akhir tertinggi : %.2f (%s)" % (tertinggi, nama_tertinggi))
print("Nilai akhir terendah  : %.2f (%s)" % (terendah, nama_terendah))
print("Rata-rata nilai akhir : %.2f" % (total_nilai_akhir / 10))
