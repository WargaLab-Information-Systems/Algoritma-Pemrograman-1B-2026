tugas = {}

while True:
    print("===========================")
    print("      MENU TO-DO LIST      ")
    print("===========================")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai dan Belum")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == 1:
        nama = input("Masukkan nama tugas: ")
        tugas[nama] = False
        print("Tugas berhasil ditambahkan!")

    elif pilihan == 2:
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            for nama in tugas:
                if tugas[nama] == True:
                    print(nama, ": Selesai")
                else:
                    print(nama, ": Belum selesai")

    elif pilihan == 3:
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            tugas[nama] = True
            print("Tugas berhasil diselesaikan!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == 4:
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == 5:
        selesai = 0

        for nama in tugas:
            if tugas[nama] == True:
                selesai = selesai + 1

        belum = len(tugas) - selesai

        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilihan == 6:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")