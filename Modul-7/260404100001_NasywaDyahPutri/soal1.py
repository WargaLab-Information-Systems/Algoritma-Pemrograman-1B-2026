# Dictionary kosong
todo_list = {}

while True:
    print("\n== MENU TO-DO LIST ==")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Hitung Tugas Selesai dan Belum Selesai")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    #nambah tugas
    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")

        if nama in todo_list:
            print("Tugas sudah ada!")
        else:
            todo_list[nama] = "Belum Selesai"
            print("Tugas berhasil ditambahkan!")

    #nampilkan semua tugas
    elif pilihan == "2":
        print("\n== DAFTAR TUGAS ==")

        if not todo_list:
            print("Belum ada tugas.")
        else:
            for tugas, status in todo_list.items():
                print(f"{tugas} : {status}")

    #nandai tugas selesai
    elif pilihan == "3":
        nama = input("Masukkan nama tugas yang selesai: ")

        if nama in todo_list:
            todo_list[nama] = "Selesai"
            print("Tugas berhasil ditandai selesai!")
        else:
            print("Tugas tidak ditemukan!")

    #hapus tugas
    elif pilihan == "4":
        nama = input("Masukkan nama tugas yang ingin dihapus: ")

        if nama in todo_list:
            del todo_list[nama]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan!")

    #hitung tugas selesai dan belum selesai
    elif pilihan == "5":
        selesai = 0
        belum_selesai = 0

        for status in todo_list.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum_selesai += 1

        print("\n== JUMLAH TUGAS ==")
        print("Tugas Selesai       :", selesai)
        print("Tugas Belum Selesai :", belum_selesai)
        print("Total Tugas         :", len(todo_list))

    #keluar dari program
    elif pilihan == "6":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-6.")
