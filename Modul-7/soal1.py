tugas = {}

while True:
    print("\nMENU TO-DO LIST")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum selesai")
    print("6. Keluar")

    try:
        pilihan = int(input("Pilih menu (1-6): "))
    except ValueError:
        print("Input harus berupa angka 1-6.")
        continue

    if pilihan == 1:
        try:
            nama = input("Masukkan nama tugas: ").strip()
            if nama == "":
                raise ValueError("Nama tugas tidak boleh kosong.")
            if nama in tugas:
                print(f"Tugas '{nama}' sudah ada.")
            else:
                tugas[nama] = "Belum Selesai"
                print(f"Tugas '{nama}' berhasil ditambahkan.")
        except ValueError as e:
            print(e)

    elif pilihan == 2:
        if not tugas:
            print("Daftar tugas masih kosong.")
        else:
            print("\nDaftar Tugas:")
            nomor = 1
            for nama, status in tugas.items():
                print(f"{nomor}. {nama} - [{status}]")
                nomor += 1

    elif pilihan == 3:
        try:
            nama = input("Masukkan nama tugas yang selesai: ").strip()
            if nama == "":
                raise ValueError("Nama tugas tidak boleh kosong.")
            status_sekarang = tugas[nama]
            if status_sekarang == "Selesai":
                print(f"Tugas '{nama}' sudah berstatus Selesai.")
            else:
                tugas[nama] = "Selesai"
                print(f"Tugas '{nama}' ditandai selesai.")
        except ValueError as e:
            print(e)
        except KeyError:
            print(f"Tugas '{nama}' tidak ditemukan.")

    elif pilihan == 4:
        try:
            nama = input("Masukkan nama tugas yang ingin dihapus: ").strip()
            if nama == "":
                raise ValueError("Nama tugas tidak boleh kosong.")
            del tugas[nama]
            print(f"Tugas '{nama}' berhasil dihapus.")
        except ValueError as e:
            print(e)
        except KeyError:
            print(f"Tugas '{nama}' tidak ditemukan.")

    elif pilihan == 5:
        selesai = 0
        belum = 0
        for status in tugas.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1
        print(f"Tugas selesai: {selesai}")
        print(f"Tugas belum selesai: {belum}")

    elif pilihan == 6:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-6.")