playlist = {}

while True:
    print("\n=== MENU PLAYLIST MUSIK ===")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Nama playlist baru: ")
        if nama == "":
            print("Nama playlist tidak boleh kosong")
        elif nama in playlist:
            print("Playlist sudah ada")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat")

    elif pilihan == "2":
        nama = input("Nama playlist: ")
        try:
            lagu = playlist[nama]
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            lagu[judul] = penyanyi
            print("Lagu berhasil ditambahkan")
        except KeyError:
            print("Playlist tidak ditemukan")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)
                if len(lagu) == 0:
                    print("  (kosong)")
                else:
                    for judul, penyanyi in lagu.items():
                        print("  -", judul, "oleh", penyanyi)

    elif pilihan == "4":
        cari = input("Judul lagu yang dicari: ")
        ditemukan = False
        for nama, lagu in playlist.items():
            if cari in lagu:
                print("Ditemukan di playlist", nama, "- penyanyi:", lagu[cari])
                ditemukan = True
        if not ditemukan:
            print("Lagu tidak ditemukan")

    elif pilihan == "5":
        nama = input("Nama playlist: ")
        try:
            lagu = playlist[nama]
        except KeyError:
            print("Playlist tidak ditemukan")
        else:
            judul = input("Judul lagu yang dihapus: ")
            try:
                del lagu[judul]
                print("Lagu berhasil dihapus")
            except KeyError:
                print("Lagu tidak ditemukan di playlist ini")

    elif pilihan == "6":
        nama = input("Nama playlist yang dihapus: ")
        try:
            del playlist[nama]
            print("Playlist berhasil dihapus")
        except KeyError:
            print("Playlist tidak ditemukan")

    elif pilihan == "7":
        print("Program selesai")
        break

    else:
        print("Menu tidak valid, pilih 1-7")