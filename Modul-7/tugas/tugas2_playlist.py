playlist = {}

while True:
    print("\n=== PLAYLIST MUSIK ===")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Nama playlist: ")
        if nama in playlist:
            print("Playlist sudah ada!")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat.")

    elif pilihan == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan.")
        else:
            print("Playlist tidak ditemukan!")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama in playlist:
                print("\nPlaylist:", nama)
                if len(playlist[nama]) == 0:
                    print("  (kosong)")
                else:
                    for judul in playlist[nama]:
                        print("  -", judul, "oleh", playlist[nama][judul])

    elif pilihan == "4":
        cari = input("Judul lagu yang dicari: ")
        ketemu = False
        for nama in playlist:
            if cari in playlist[nama]:
                print("Ditemukan di playlist", nama, "- penyanyi:", playlist[nama][cari])
                ketemu = True
        if not ketemu:
            print("Lagu tidak ditemukan!")

    elif pilihan == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu yang dihapus: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus.")
            else:
                print("Lagu tidak ditemukan di playlist ini!")
        else:
            print("Playlist tidak ditemukan!")

    elif pilihan == "6":
        nama = input("Nama playlist yang dihapus: ")
        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus.")
        else:
            print("Playlist tidak ditemukan!")

    elif pilihan == "7":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
