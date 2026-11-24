
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

total_nilai_akhir = 0
nilai_tertinggi = -1
nilai_terendah = 101
nama_tertinggi = ""
nama_terendah = ""

for i in range(1, 11):
    print(f"\n=== Mahasiswa ke-{i} ===")

    nama = input("Masukkan nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    total_nilai_akhir += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

    print("\nHasil mahasiswa:")
    print("Nama:", nama)
    print("Nilai tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print(f"Nilai akhir: {nilai_akhir:.2f}")
    print("Kategori:", kategori)

rata_rata = total_nilai_akhir / 10

print("\n=== REKAPITULASI KELAS ===")
print("Jumlah kategori A:", jumlah_A)
print("Jumlah kategori B:", jumlah_B)
print("Jumlah kategori C:", jumlah_C)
print("Jumlah kategori D:", jumlah_D)
print("Jumlah kategori E:", jumlah_E)

print("\nNilai tertinggi:", nama_tertinggi,
      f"({nilai_tertinggi:.2f})")

print("Nilai terendah:", nama_terendah,
      f"({nilai_terendah:.2f})")

print(f"Rata-rata nilai kelas: {rata_rata:.2f}")
