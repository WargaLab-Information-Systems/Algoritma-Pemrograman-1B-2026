jumlahA = 0
jumlahB = 0
jumlahC = 0
jumlahD = 0
jumlahE = 0

totalNilai = 0
nilaiMax = -1
nilaiMin = 101
namaMax = ""
namaMin = ""

print("Masukkan Data 10 Mahasiswa")

for i in range(1, 11):
    nama = input(f"\nMahasiswa {i} - Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    totalNilai = totalNilai + akhir
    
    if akhir >= 85:
        kategori = 'A'
        jumlahA = jumlahA + 1
    elif akhir >= 75:
        kategori = 'B'
        jumlahB = jumlahB + 1
    elif akhir >= 65:
        kategori = 'C'
        jumlahC = jumlahC + 1
    elif akhir >= 50:
        kategori = 'D'
        jumlahD = jumlahD + 1
    else:
        kategori = 'E'
        jumlahE = jumlahE + 1
        
    if akhir > nilaiMax:
        nilaiMax = akhir
        namaMax = nama
        
    if akhir < nilaiMin:
        nilaiMin = akhir
        namaMin = nama
        
    print(f"{i}. Nama: {nama} | Tugas: {tugas} | UTS: {uts} | UAS: {uas} | Akhir: {akhir} | Kategori: {kategori}")

print("\n JAWABAN")
print(f"Kategori A: {jumlahA}")
print(f"Kategori B: {jumlahB}")
print(f"Kategori C: {jumlahC}")
print(f"Kategori D: {jumlahD}")
print(f"Kategori E: {jumlahE}")
print(f"Tertinggi : {namaMax} ({nilaiMax})")
print(f"Terendah  : {namaMin} ({nilaiMin})")
print(f"Rata-rata : {totalNilai / 10}")
