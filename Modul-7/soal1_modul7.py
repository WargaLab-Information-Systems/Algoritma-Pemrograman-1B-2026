tugas = {}

while True:
    print("\n1.Tambah  2.Lihat  3.Selesai  4.Hapus  5.Rekap  6.Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum"
    elif pilih == "2":
        for k, v in tugas.items():
            print(k, ":", v)
    elif pilih == "3":
        nama = input("Tugas selesai: ")
        try:
            cek = tugas[nama]
            tugas[nama] = "Selesai"
        except KeyError:
            print("Tugas tidak ada!")
    elif pilih == "4":
        nama = input("Hapus tugas: ")
        try:
            del tugas[nama]
        except KeyError:
            print("Tugas tidak ada!")
    elif pilih == "5":
        selesai = list(tugas.values()).count("Selesai")
        belum = len(tugas) - selesai
        print("Selesai:", selesai, "| Belum:", belum)
    elif pilih == "6":
        break