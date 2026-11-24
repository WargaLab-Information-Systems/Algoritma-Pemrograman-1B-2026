
# Input nama asisten awal
asisten = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten.append(nama)

# Mengubah list menjadi tuple
asisten_awal = tuple(asisten)

# Input asisten tambahan
tambahan = input("\nMasukkan nama asisten tambahan: ")

# Menggabungkan tuple
asisten_akhir = asisten_awal + (tambahan,)

# Input hari tugas
hari = []

while True:
    nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

    if nama_hari.lower() == "cukup":
        break

    hari.append(nama_hari)

# Mengubah hari menjadi tuple
hari_tugas = tuple(hari)

# Input pengecualian
pengecualian_asisten = input("\nMasukkan nama asisten pengecualian: ")
pengecualian_hari = input("Masukkan hari pengecualian: ")

# Menampilkan jadwal
print("\nJadwal Shift Asisten:")

for a in asisten_akhir:
    for h in hari_tugas:

        if a == pengecualian_asisten and h == pengecualian_hari:
            continue

        print(a, "-", h)
