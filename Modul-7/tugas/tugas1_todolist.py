todo = {}

while True:
    print("\n====================")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai & belum")
    print("6. Keluar")
    print("====================")
    pilihan = input("\nPilih menu (1-6): ")

    if pilihan == "1":
        nama = input("Nama tugas: ")
        if nama in todo:
            print("Tugas sudah ada!")
        else:
            todo[nama] = "Belum selesai"
            print("Tugas berhasil ditambahkan.")

    elif pilihan == "2":
        if len(todo) == 0:
            print("Belum ada tugas.")
        else:
            nomor = 1
            for nama in todo:
                print(nomor, ".", nama, "-", todo[nama])
                nomor += 1

    elif pilihan == "3":
        nama = input("Nama tugas yang selesai: ")
        if nama in todo:
            todo[nama] = "Selesai"
            print("Tugas ditandai selesai.")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "4":
        nama = input("Nama tugas yang dihapus: ")
        if nama in todo:
            del todo[nama]
            print("Tugas berhasil dihapus.")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "5":
        selesai = 0
        belum = 0
        for nama in todo:
            if todo[nama] == "Selesai":
                selesai += 1
            else:
                belum += 1
        print("Tugas selesai :", selesai)
        print("Tugas belum   :", belum)

    elif pilihan == "6":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
