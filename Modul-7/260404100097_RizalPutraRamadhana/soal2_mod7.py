playlist = {}

while True:
    print(" PLAYLIST MUSIC")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Lihat playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        playlist[nama] = {}
        print("Playlist berhasil dibuat.")

    elif pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Nama penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "3":
        for nama, lagu in playlist.items():
            print("Playlist:", nama)
            for judul, penyanyi in lagu.items():
                print(judul, "-", penyanyi)

    elif pilih == "4":
        cari = input("Judul lagu: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            if cari in lagu:
                print(cari, "-", lagu[cari], "(", nama, ")")
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan.")

    elif pilih == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus.")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "6":
        nama = input("Nama playlist: ")
        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilih == "7":
        break

    else:
        print("Pilihan tidak valid.")