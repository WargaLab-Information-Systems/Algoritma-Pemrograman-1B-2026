playlist = {}

while True:
    print("\nMENU PLAYLIST MUSIK")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist dan lagu")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")

    try:
        pilihan = int(input("Pilih menu (1-7): "))
    except ValueError:
        print("Input harus berupa angka 1-7.")
        continue

    if pilihan == 1:
        try:
            nama_pl = input("Masukkan nama playlist: ").strip()
            if nama_pl == "":
                raise ValueError("Nama playlist tidak boleh kosong.")
            if nama_pl in playlist:
                print(f"Playlist '{nama_pl}' sudah ada.")
            else:
                playlist[nama_pl] = {}
                print(f"Playlist '{nama_pl}' berhasil dibuat.")
        except ValueError as e:
            print(e)

    elif pilihan == 2:
        try:
            nama_pl = input("Masukkan nama playlist tujuan: ").strip()
            if nama_pl == "":
                raise ValueError("Nama playlist tidak boleh kosong.")
            target_pl = playlist[nama_pl]
            judul = input("Masukkan judul lagu: ").strip()
            penyanyi = input("Masukkan nama penyanyi: ").strip()
            if judul == "" or penyanyi == "":
                raise ValueError("Judul lagu dan penyanyi tidak boleh kosong.")
            if judul in target_pl:
                print(f"Lagu '{judul}' sudah ada di playlist '{nama_pl}'.")
            else:
                target_pl[judul] = penyanyi
                print(f"Lagu '{judul}' - {penyanyi} ditambahkan ke '{nama_pl}'.")
        except ValueError as e:
            print(e)
        except KeyError:
            print(f"Playlist '{nama_pl}' tidak ditemukan.")

    elif pilihan == 3:
        if not playlist:
            print("Belum ada playlist.")
        else:
            print("\nDaftar Playlist:")
            for nama_pl, lagu_dict in playlist.items():
                print(f"- {nama_pl}")
                if not lagu_dict:
                    print("  (Playlist kosong)")
                else:
                    nomor = 1
                    for judul, penyanyi in lagu_dict.items():
                        print(f"  {nomor}. {judul} - {penyanyi}")
                        nomor += 1

    elif pilihan == 4:
        if not playlist:
            print("Belum ada playlist.")
        else:
            try:
                cari = input("Masukkan judul lagu yang dicari: ").strip()
                if cari == "":
                    raise ValueError("Judul lagu tidak boleh kosong.")
                ditemukan = False
                for nama_pl, lagu_dict in playlist.items():
                    if cari in lagu_dict:
                        print(f"Ditemukan di '{nama_pl}': {cari} - {lagu_dict[cari]}")
                        ditemukan = True
                if not ditemukan:
                    print(f"Lagu '{cari}' tidak ditemukan di playlist manapun.")
            except ValueError as e:
                print(e)

    elif pilihan == 5:
        try:
            nama_pl = input("Masukkan nama playlist: ").strip()
            if nama_pl == "":
                raise ValueError("Nama playlist tidak boleh kosong.")
            target_pl = playlist[nama_pl]
            try:
                judul = input("Masukkan judul lagu yang ingin dihapus: ").strip()
                if judul == "":
                    raise ValueError("Judul lagu tidak boleh kosong.")
                del target_pl[judul]
                print(f"Lagu '{judul}' berhasil dihapus dari '{nama_pl}'.")
            except KeyError:
                print(f"Lagu '{judul}' tidak ditemukan di playlist '{nama_pl}'.")
        except ValueError as e:
            print(e)
        except KeyError:
            print(f"Playlist '{nama_pl}' tidak ditemukan.")

    elif pilihan == 6:
        try:
            nama_pl = input("Masukkan nama playlist yang ingin dihapus: ").strip()
            if nama_pl == "":
                raise ValueError("Nama playlist tidak boleh kosong.")
            del playlist[nama_pl]
            print(f"Playlist '{nama_pl}' berhasil dihapus.")
        except ValueError as e:
            print(e)
        except KeyError:
            print(f"Playlist '{nama_pl}' tidak ditemukan.")

    elif pilihan == 7:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-7.")
