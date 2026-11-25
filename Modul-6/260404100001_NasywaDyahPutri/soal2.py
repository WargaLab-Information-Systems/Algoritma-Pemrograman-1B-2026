daftar_asisten = [ ]

while True:
    nama_asis = input("Masukkan nama asisten (ketik 'cukup' untuk berhenti): ")
    if nama_asis == "cukup":
        break
    daftar_asisten.append(nama_asis)

asisten_awal = tuple(daftar_asisten)
asisten_baru = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (asisten_baru, )

daftar_hari = [ ]

while True:
    hari = input("Masukkan nama hari (ketik 'cukup' untuk berhenti): ")
    if hari == "cukup":
        break
    daftar_hari.append(hari)

hari_tetap = tuple(daftar_hari)

asisten_kecuali = input("\nMasukkan nama asisten pengecualian: ")
hari_kecuali = input("Masukkan hari pengecualian: ")

jadwal = []
for asisten in asisten_akhir:
    for hari in hari_tetap:
        if asisten == asisten_kecuali and hari == hari_kecuali:
            continue  # lewati kombinasi pengecualian
        jadwal.append((asisten, hari))

# Langkah 7: tampilkan hasil
print("\n--- Jadwal Shift ---")
for asisten, hari in jadwal:
    print(f"{asisten} - {hari}")

print(f"Total shift berhasil dibuat: {len(jadwal)}")