kategori = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
total_nilai = 0
tertinggi = terendah = 0
nama_tertinggi = nama_terendah = ""

for i in range(10):
    print(f"\nMahasiswa ke-{i + 1}")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        grade = "A"
    elif akhir >= 75:
        grade = "B"
    elif akhir >= 65:
        grade = "C"
    elif akhir >= 50:
        grade = "D"
    else:
        grade = "E"

    kategori[grade] += 1
    total_nilai += akhir

    print(f"{nama} | Tugas {tugas} | UTS {uts} | UAS {uas} | "
          f"Akhir {akhir:.2f} | Kategori {grade}")

    if i == 0 or akhir > tertinggi:
        tertinggi, nama_tertinggi = akhir, nama
    if i == 0 or akhir < terendah:
        terendah, nama_terendah = akhir, nama

for g in kategori:
    print(f"Jumlah nilai {g}: {kategori[g]}")
print(f"Nilai tertinggi : {tertinggi:.2f} ({nama_tertinggi})")
print(f"Nilai terendah  : {terendah:.2f} ({nama_terendah})")
print(f"Rata-rata       : {total_nilai / 10:.2f}")