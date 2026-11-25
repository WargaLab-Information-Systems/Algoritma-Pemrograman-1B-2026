jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

nama_tertinggi = ""
nama_terendah = ""
tertinggi = 0
terendah = 101

total_semua_nilai = 0

for mahasiswa in range(1,11):
    nama = input("masukkan nama mahasiswa = ")
    tugas = int(input("masukkan nilai tugas = "))
    tugas_h = tugas * 30 / 100
    print("nilai tugas = ", tugas_h)
    uts = int(input("masukkan nilai uts = "))
    uts_h = uts * 30 / 100
    print("nilai uts = ", uts_h)
    uas = int(input("masukkan nilai uas ="))
    uas_h = uas * 40 / 100
    print("nilai uas = ", uas_h)
    total_nilai = tugas_h + uts_h + uas_h
    print(f"total nilai {nama} = {total_nilai}")

    if total_nilai > 100 :
        print("tidak valid")
    elif total_nilai >= 85 :
        print("mendapatkan nilai A")
        jumlah_a += 1
    elif total_nilai >= 75 :
        print("mendapatkan nilai B")
        jumlah_b += 1
    elif total_nilai >= 65 :
        print("mendapatkan nilai C")
        jumlah_c += 1
    elif total_nilai >= 50 :
        print("mendapatkan nilai D")
        jumlah_d += 1
    else:
        print("mendapatkan nilai E")
        jumlah_e += 1

    if total_nilai > tertinggi:
        tertinggi = total_nilai
        nama_tertinggi = nama

    if total_nilai < terendah:
        terendah = total_nilai
        nama_terendah = nama

    total_semua_nilai += total_nilai

    print("mahasiswa ke = ", mahasiswa)

print("total mahasiswa mendapatkan nilai A =", jumlah_a)
print("total mahasiswa mendapatkan nilai B =", jumlah_b)
print("total mahasiswa mendapatkan nilai C =", jumlah_c)
print("total mahasiswa mendapatkan nilai D =", jumlah_d)
print("total mahasiswa mendapatkan nilai E =", jumlah_e)
print(f"nilai tertinggi = {tertinggi} dengan nama = {nama_tertinggi}")
print(f"nilai terendah = {terendah} dengan nama = {nama_terendah}")
print("rata rata nilai = ", total_semua_nilai / mahasiswa)