anggota = []

# Memasukkan nama anggota
while True:
    nama = input("Masukkan nama anggota : ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

# Memeriksa setiap nama
print("=== HASIL PEMERIKSAAN ===")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")

# Menghapus nama yang dicurigai
penyusup = input("Masukkan nama yang dicurigai: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan, tidak ada yang dihapus.")

# Menampilkan daftar akhir
print("=====ANGGOTA AKHIRNYA=====")
print(anggota)