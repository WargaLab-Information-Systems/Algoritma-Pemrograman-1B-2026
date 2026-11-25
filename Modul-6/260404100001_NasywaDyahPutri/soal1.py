daftar_nama = [ ]

while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    daftar_nama.append(nama)

for nama in daftar_nama:
    if nama == "admin" or len(nama) < 4:
        print(f"Nama, '{nama}' tidak valid")
    else:
        print(f"Nama , '{nama}', Valid")

penyusup = input("Masukkan nama yang dicurigai: ")

if penyusup in daftar_nama:
    daftar_nama.remove(penyusup)
    print(f"Nama, '{penyusup}' sudah dihapus")

else: 
    print(f"Nama '{penyusup}' tidak ditemukan di pendaftaran.")


print("Daftar anggota terbaru", daftar_nama)