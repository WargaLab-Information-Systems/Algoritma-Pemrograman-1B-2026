asisten_awal = []

# Memasukkan asisten awal
while True:
    nama = input("Masukkan nama asisten awal: ")

    if nama.lower() == "cukup":
        break

    asisten_awal.append(nama)
asisten_akhir = asisten_awal.copy()

# Menambahkan asisten baru
tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir.append(tambahan)

# Memasukkan daftar hari tugas
hari = []

while True:
    tanggal = input("Masukkan hari tugas : ")

    if tanggal.lower() == "cukup":
        break

    hari.append(tanggal)

# Memasukkan pengecualian
print("=== PENGECUALIAN ===")
nama_izin = input("Nama asisten yang izin: ")
hari_izin = input("Hari pengecualian: ")

# Membuat jadwal shift
print("=== JADWAL SHIFT ===")

for nama in asisten_akhir:
    for tanggal in hari:
        if nama == nama_izin and tanggal == hari_izin:
            continue

        print(nama, "-", tanggal)