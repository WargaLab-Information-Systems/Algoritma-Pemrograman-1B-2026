daftar_anggota = []
while True :
    nama = input("nama calon anggota: ")
    if nama == ("selesai"):
        print("program selesai")
        break
    daftar_anggota.append(nama)
    if len(nama) < 4 or nama == "admin":
        print("nama tidak valid")
        continue
print("=========================")
print("daftar anggota: ", daftar_anggota)
print("=========================")
print("masukin nama yang di curigain")
nama_curiga = input("nama: ")
if nama_curiga in daftar_anggota:
    daftar_anggota.remove(nama_curiga)
    print("daftar anggota: ", daftar_anggota)
else:
    print("nama tersebut tidak ditemukan")