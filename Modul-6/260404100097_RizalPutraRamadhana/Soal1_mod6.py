anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik 'selesai' untuk berhenti): ")
    if nama.lower() == "selesai":
        break
    anggota.append(nama)

print("\n--- HASIL PEMERIKSAAN NAMA ---")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus.")
else:
    print("Nama", penyusup, "tidak ditemukan dalam pendaftaran.")

print("\n--- DAFTAR ANGGOTA AKHIR ---")
print(anggota)