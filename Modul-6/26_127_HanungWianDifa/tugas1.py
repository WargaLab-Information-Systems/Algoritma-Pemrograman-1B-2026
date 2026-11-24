
# Membuat list untuk menyimpan nama anggota
anggota = []

# Input nama anggota
while True:
    nama = input("Masukkan nama anggota (selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

# Memeriksa nama anggota
print("\nHasil pemeriksaan:")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

# Menghapus nama penyusup
penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus.")
else:
    print("Nama penyusup tidak ditemukan.")

# Menampilkan daftar akhir
print("\nDaftar anggota akhir:", anggota)
