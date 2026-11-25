dodo = {}

while True:
    print("DO-DO LIST")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Tandai selesai")
    print("4. Hapus tugas")
    print("5. Hitung tugas")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tugas = input("Nama tugas: ")
        dodo[tugas] = "Belum selesai"
        print("Tugas berhasil ditambahkan.")

    elif pilih == "2":
        if not dodo:
            print("Belum ada tugas.")
        else:
            for tugas, status in dodo.items():
                print(tugas, "-", status)

    elif pilih == "3":
        tugas = input("Nama tugas: ")
        if tugas in dodo:
            dodo[tugas] = "Selesai"
            print("Tugas berhasil diselesaikan.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "4":
        tugas = input("Nama tugas: ")
        if tugas in dodo:
            del dodo[tugas]
            print("Tugas berhasil dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilih == "5":
        selesai = 0
        belum = 0

        for status in dodo.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1

        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilih == "6":
        break

    else:
        print("Pilihan tidak valid.")