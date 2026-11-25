asisten_awal = []

while True:
    nama = input("Masukkan nama asisten (ketik cukup): ")
    if nama.lower() == "cukup":
        break
    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)
tambahan = input("\nMasukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

hari = []

while True:
    nama_hari = input("Masukkan hari tugas (ketik cukup): ")
    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

hari = tuple(hari)
print("\n=== DATA PENGECUALIAN ===")
nama_izin = input("Nama asisten yang dikecualikan: ")
hari_izin = input("Hari yang dikecualikan: ")

print("\n=== JADWAL SHIFT ===")

for asisten in asisten_akhir:
    for h in hari:
        if asisten == nama_izin and h == hari_izin:
            continue

        print(asisten, "-", h)