anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik selesai): ")
    if nama.lower() == "selesai":
        break

    anggota.append(nama)

print("\n=== HASIL PEMERIKSAAN ===")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")
    
if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama berhasil dihapus.")
else:
    print("Nama tidak ditemukan.")

print("\nDaftar anggota akhir:", anggota)