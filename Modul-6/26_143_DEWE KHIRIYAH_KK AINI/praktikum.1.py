daftar_nama = []

while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    daftar_nama.append(nama)

print("\n--- Hasil Evaluasi ---")

for nama in daftar_nama:
    if nama.lower() == "admin" or len(nama) < 4: 
        print(nama, "-> Nama tidak valid")
    else: 
        print(nama, "-> Nama valid")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

try:
    daftar_nama.remove(penyusup)
    print(penyusup, "berhasil dihapus dari sistem.")
except ValueError:
    print(penyusup, "tidak ditemukan dalam daftar, sehingga tidak ada data yang dihapus.")

print("\n--- Daftar Anggota Setelah Penghapusan ---")
for nama in daftar_nama:
     print(nama)