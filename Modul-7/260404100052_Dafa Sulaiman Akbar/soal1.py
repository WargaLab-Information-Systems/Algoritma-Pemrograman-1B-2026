todo = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("Nama tugas: ")
        if nama == "":
            print("Nama tugas tidak boleh kosong")
        elif nama in todo:
            print("Tugas sudah ada")
        else:
            todo[nama] = "Belum"
            print("Tugas berhasil ditambahkan")

    elif pilihan == "2":
        if len(todo) == 0:
            print("Belum ada tugas")
        else:
            nomor = 1
            for nama, status in todo.items():
                print(nomor, ".", nama, "-", status)
                nomor += 1

    elif pilihan == "3":
        nama = input("Nama tugas yang selesai: ")
        try:
            todo[nama]
            todo[nama] = "Selesai"
            print("Tugas ditandai selesai")
        except KeyError:
            print("Tugas tidak ditemukan")

    elif pilihan == "4":
        nama = input("Nama tugas yang dihapus: ")
        try:
            del todo[nama]
            print("Tugas berhasil dihapus")
        except KeyError:
            print("Tugas tidak ditemukan")

    elif pilihan == "5":
        selesai = 0
        belum = 0
        for status in todo.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1
        print("Tugas selesai :", selesai)
        print("Tugas belum   :", belum)

    elif pilihan == "6":
        print("Program selesai")
        break

    else:
        print("Menu tidak valid, pilih 1-6")