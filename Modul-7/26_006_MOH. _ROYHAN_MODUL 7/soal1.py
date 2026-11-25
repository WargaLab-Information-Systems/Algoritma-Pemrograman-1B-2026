todo = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai dan Belum")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tugas = input("Masukkan nama tugas: ")
        todo[tugas] = "Belum Selesai"
        print("Tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if not todo:
            print("Belum ada tugas.")
        else:
            for tugas, status in todo.items():
                print(tugas, ":", status)

    elif pilihan == "3":
        tugas = input("Masukkan nama tugas: ")
        if tugas in todo:
            todo[tugas] = "Selesai"
            print("Tugas berhasil diselesaikan!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "4":
        tugas = input("Masukkan nama tugas: ")
        if tugas in todo:
            del todo[tugas]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "5":
        selesai = list(todo.values()).count("Selesai")
        belum = list(todo.values()).count("Belum Selesai")
        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")