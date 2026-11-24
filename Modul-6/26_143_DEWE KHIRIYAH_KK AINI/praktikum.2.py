
asisten_awal = []

while True:
    nama = input("Masukkan nama asisten (ketik 'cukup' untuk selesai): ")

    if nama.lower() == "cukup":
        break

    asisten_awal.append(nama)

asisten_awal = tuple(asisten_awal)

tambahan = input("Masukkan nama asisten tambahan: ")

asisten_akhir = list(asisten_awal) + [tambahan]

hari_tugas = []

while True:
    hari = input("Masukkan hari tugas (ketik 'cukup' untuk selesai): ")

    if hari.lower() == "cukup":
        break

    hari_tugas.append(hari)

hari_tugas = tuple(hari_tugas)

nama_pengecualian = input("\nMasukkan nama asisten yang dikecualikan: ")
hari_pengecualian = input("Masukkan hari yang dikecualikan: ")

print("\n=== JADWAL SHIFT ASISTEN ===")

for asisten in asisten_akhir:
    for hari in hari_tugas:

        if asisten == nama_pengecualian and hari == hari_pengecualian:
            continue

        print(asisten, "-", hari) 