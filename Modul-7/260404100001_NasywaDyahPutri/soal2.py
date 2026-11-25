# Dictionary utama kosong
playlist = {}

while True:
    print("\n== MENU PENGELOLA PLAYLIST MUSIK ==")
    print("1. Membuat Playlist")
    print("2. Menambah Lagu ke Playlist")
    print("3. Menampilkan Semua Playlist")
    print("4. Mencari Lagu")
    print("5. Menghapus Lagu dari Playlist")
    print("6. Menghapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    #buat playlist
    if pilihan == "1":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            print("Playlist sudah tersedia!")
        else:
            playlist[nama_playlist] = {}
            print("Playlist berhasil dibuat!")

    #nambah lagu ke playlist
    elif pilihan == "2":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            if judul in playlist[nama_playlist]:
                print("Lagu sudah ada di playlist!")
            else:
                playlist[nama_playlist][judul] = penyanyi
                print("Lagu berhasil ditambahkan!")
        else:
            print("Playlist tidak ditemukan!")

    #nampilkan semua playlist
    elif pilihan == "3":
        print("\n== DAFTAR SEMUA PLAYLIST ==")

        if not playlist:
            print("Belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print(f"\nPlaylist: {nama}")

                if not lagu:
                    print("  Belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print(f"  - {judul} | Penyanyi: {penyanyi}")

    #cari lagu
    elif pilihan == "4":
        cari = input("Masukkan judul lagu yang dicari: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            if cari in lagu:
                print("\nLagu ditemukan!")
                print("Judul Lagu :", cari)
                print("Penyanyi   :", lagu[cari])
                print("Playlist   :", nama)
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan!")

    #hapus lagu dari playlist
    elif pilihan == "5":
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul = input("Masukkan judul lagu yang dihapus: ")

            if judul in playlist[nama_playlist]:
                del playlist[nama_playlist][judul]
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan dalam playlist!")
        else:
            print("Playlist tidak ditemukan!")

    #hapus playlist
    elif pilihan == "6":
        nama_playlist = input("Masukkan nama playlist yang dihapus: ")

        if nama_playlist in playlist:
            del playlist[nama_playlist]
            print("Playlist berhasil dihapus!")
        else:
            print("Playlist tidak ditemukan!")

    #Keluar
    elif pilihan == "7":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-7.")
