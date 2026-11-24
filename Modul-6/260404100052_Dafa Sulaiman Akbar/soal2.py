asisten_list = []
while True:
    nama = input("Masukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")
    if nama == "cukup":
        break
    asisten_list.append(nama)
asisten_awal = tuple(asisten_list)

tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

hari_list = []
while True:
    hari = input("Masukkan hari tugas (ketik 'cukup' untuk berhenti): ")
    if hari == "cukup":
        break
    hari_list.append(hari)
hari_tugas = tuple(hari_list)

nama_kecuali = input("Masukkan nama asisten pengecualian: ")
hari_kecuali = input("Masukkan hari pengecualian: ")

print()
print("=== Jadwal Shift ===")
jumlah = 0
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if not (asisten == nama_kecuali and hari == hari_kecuali):
            print(f"{asisten} - {hari}")
            jumlah = jumlah + 1

print(f"Total shift yang berhasil dibuat: {jumlah}")