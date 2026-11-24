daftar = []

while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    daftar.append(nama)

print()
print("=== Hasil Pemeriksaan ===")
for nama in daftar:
    if nama.lower() == "admin" or len(nama) < 4:
        print(f"{nama} : nama tidak valid")
    else:
        print(f"{nama} : valid")

print()
penyusup = input("Masukkan nama penyusup yang akan dihapus: ")
if penyusup in daftar:
    daftar.remove(penyusup)
    print(f"Nama {penyusup} berhasil dihapus")
else:
    print(f"Nama {penyusup} tidak ditemukan di pendaftaran")

print("Daftar anggota sekarang:", daftar)