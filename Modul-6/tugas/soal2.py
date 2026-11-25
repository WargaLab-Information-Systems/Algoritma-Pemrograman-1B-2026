asisten_awal = []
while True:
    nama = input("Masukkan nama asisten: ")
    if nama == "cukup":
        break
    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)
tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = list(asisten_awal) + [tambahan]

hari = []
while True:
    nama_hari = input("Masukkan hari tugas: ")
    if nama_hari == "cukup":
        break
    hari.append(nama_hari)
hari = tuple(hari)

nama_pengecualian = input("Nama asisten yang dikecualikan: ")
hari_pengecualian = input("Hari yang dikecualikan: ")
print("\nDaftar jadwal shift:")

for nama in asisten_akhir:
    for nama_hari in hari:
        if nama != nama_pengecualian or nama_hari != hari_pengecualian:
            print(nama, "-", nama_hari)