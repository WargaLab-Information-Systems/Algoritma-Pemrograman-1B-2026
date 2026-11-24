playlist = {}

while True:
    print("\n1.Buat PL  2.Tambah Lagu  3.Lihat  4.Cari  5.Hapus Lagu  6.Hapus PL  7.Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        pl = input("Nama playlist: ")
        playlist[pl] = {}
    elif pilih == "2":
        pl = input("Playlist tujuan: ")
        try:
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[pl][judul] = penyanyi
        except KeyError:
            print("Playlist tidak ada!")
    elif pilih == "3":
        for pl, lagu in playlist.items():
            print("Playlist:", pl, "->", lagu)
    elif pilih == "4":
        cari = input("Cari judul lagu: ")
        for pl, lagu in playlist.items():
            if cari in lagu:
                print("Ada di", pl, "- Penyanyi:", lagu[cari])
    elif pilih == "5":
        pl = input("Nama playlist: ")
        judul = input("Judul lagu: ")
        try:
            del playlist[pl][judul]
        except KeyError:
            print("Data tidak ditemukan!")
    elif pilih == "6":
        pl = input("Hapus playlist: ")
        try:
            del playlist[pl]
        except KeyError:
            print("Playlist tidak ada!")
    elif pilih == "7":
        break