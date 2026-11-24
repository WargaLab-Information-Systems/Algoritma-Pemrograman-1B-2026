def tampilkan_menu():
    print("\n--- APLIKASI PENGELOLA PLAYLIST MUSIK ---")
    print("1. Buat Playlist Baru")
    print("2. Tambah Lagu ke Playlist")
    print("3. Tampilkan Semua Playlist & Lagu")
    print("4. Cari Lagu")
    print("5. Hapus Lagu dari Playlist")
    print("6. Hapus Playlist")
    print("7. Keluar")

def main():
    # Dictionary utama yang awalnya kosong
    # Format: { nama_playlist: { judul_lagu: penyanyi, ... }, ... }
    music_library = {}

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            # 1. Buat Playlist Baru
            nama_playlist = input("Masukkan nama playlist baru: ")
            if not nama_playlist:
                print("Nama playlist tidak boleh kosong!")
                continue
            
            if nama_playlist in music_library:
                print(f"Playlist '{nama_playlist}' sudah ada.")
            else:
                # Membuat dictionary kosong di dalam dictionary utama untuk playlist baru
                music_library[nama_playlist] = {}
                print(f"Playlist '{nama_playlist}' berhasil dibuat!")

        elif pilihan == '2':
            # 2. Tambah Lagu ke Playlist
            if not music_library:
                print("\nBelum ada playlist yang tersedia. Buat playlist terlebih dahulu (Menu 1).")
                continue
            
            nama_playlist = input("Masukkan nama playlist yang dituju: ")
            
            # Cek apakah playlist ada untuk mencegah error
            if nama_playlist in music_library:
                judul_lagu = input("Masukkan judul lagu: ")
                penyanyi = input("Masukkan nama penyanyi/artist: ")
                
                if not judul_lagu or not penyanyi:
                    print("Judul lagu dan penyanyi tidak boleh kosong!")
                    continue
                
                # Menambahkan lagu ke dictionary playlist tersebut
                music_library[nama_playlist][judul_lagu] = penyanyi
                print(f"Lagu '{judul_lagu}' oleh {penyanyi} berhasil ditambahkan ke playlist '{nama_playlist}'.")
            else:
                print(f"Error: Playlist '{nama_playlist}' tidak ditemukan.")

        elif pilihan == '3':
            # 3. Tampilkan Semua Playlist & Lagu
            if not music_library:
                print("\nBelum ada playlist di dalam library.")
            else:
                print("\n--- DAFTAR PLAYLIST MUSIK ---")
                for playlist, lagu_dict in music_library.items():
                    print(f"\n🎵 Playlist: {playlist}")
                    if not lagu_dict:
                        print("   (Playlist ini masih kosong)")
                    else:
                        for index, (judul, penyanyi) in enumerate(lagu_dict.items(), 1):
                            print(f"   {index}. {judul} - {penyanyi}")

        elif pilihan == '4':
            # 4. Cari Lagu
            if not music_library:
                print("\nLibrary musik masih kosong.")
                continue
            
            cari_judul = input("Masukkan judul lagu yang ingin dicari: ").lower()
            ditemukan = False
            
            print(f"\n--- HASIL PENCARIAN: '{cari_judul}' ---")
            for playlist, lagu_dict in music_library.items():
                for judul, penyanyi in lagu_dict.items():
                    # Pencarian menggunakan .lower() agar tidak case-sensitive
                    if cari_judul in judul.lower():
                        print(f"- Lagu: {judul} (Penyanyi: {penyanyi}) ➔ Ditemukan di playlist: [{playlist}]")
                        ditemukan = True
            
            if not ditemukan:
                print(f"Lagu dengan judul yang mengandung '{cari_judul}' tidak ditemukan di playlist manapun.")

        elif pilihan == '5':
            # 5. Hapus Lagu dari Playlist
            if not music_library:
                print("\nBelum ada playlist.")
                continue
            
            nama_playlist = input("Masukkan nama playlist asal lagu: ")
            
            # Cek keberadaan playlist
            if nama_playlist in music_library:
                if not music_library[nama_playlist]:
                    print(f"Playlist '{nama_playlist}' sudah kosong.")
                    continue
                
                judul_lagu = input("Masukkan judul lagu yang ingin dihapus: ")
                
                # Cek keberadaan lagu di dalam dictionary playlist tersebut
                if judul_lagu in music_library[nama_playlist]:
                    del music_library[nama_playlist][judul_lagu]
                    print(f"Lagu '{judul_lagu}' berhasil dihapus dari playlist '{nama_playlist}'.")
                else:
                    print(f"Error: Lagu '{judul_lagu}' tidak ditemukan di dalam playlist '{nama_playlist}'.")
            else:
                print(f"Error: Playlist '{nama_playlist}' tidak ditemukan.")

        elif pilihan == '6':
            # 6. Hapus Playlist
            if not music_library:
                print("\nBelum ada playlist.")
                continue
            
            nama_playlist = input("Masukkan nama playlist yang ingin dihapus total: ")
            
            # Cek keberadaan playlist untuk mencegah KeyError
            if nama_playlist in music_library:
                del music_library[nama_playlist]
                print(f"Playlist '{nama_playlist}' beserta seluruh isinya berhasil dihapus.")
            else:
                print(f"Error: Playlist '{nama_playlist}' tidak ditemukan.")

        elif pilihan == '7':
            print("\nTerima kasih telah menggunakan aplikasi Playlist Musik!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 7.")

if __name__ == "__main__":
    main()