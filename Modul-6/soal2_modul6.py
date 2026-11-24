asisten_awal = []
while True:
    nama = input("Masukkan nama asisten (cukup untuk selesai): ")

    if nama.lower() == "cukup":
        break

    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)

print("\nMasukkan asisten tambahan:")
asisten_baru = input("Nama asisten tambahan: ")

asisten_akhir = asisten_awal + (asisten_baru,)

hari_tugas = []

while True:
    hari = input("Masukkan hari tugas (cukup untuk selesai): ")

    if hari.lower() == "cukup":
        break

    hari_tugas.append(hari)

hari_tugas = tuple(hari_tugas)

print("\nMasukkan data pengecualian:")
nama_izin = input("Nama asisten yang dikecualikan: ")
hari_izin = input("Hari yang dikecualikan: ")

print("\n=== JADWAL SHIFT ASISTEN LABORATORIUM ===")

for nama in asisten_akhir:
    for hari in hari_tugas:

        if nama == nama_izin and hari == hari_izin:
            continue

        print(nama, "-", hari)
