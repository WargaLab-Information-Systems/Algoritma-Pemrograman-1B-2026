def tampilkan_menu():
    print("\n--- APLIKASI TO-DO LIST ---")
    print("1. Tambah Tugas")
    print("2. Tampilkan Semua Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Tampilkan Statistik Tugas (Selesai/Belum)")
    print("6. Keluar")

def main():
    # Dictionary awal kosong dengan format: {nama_tugas: status_tugas}
    todo_list = {}

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ") 

        if pilihan == '1':
            # 1. Tambah Tugas
            nama_tugas = input("Masukkan nama tugas baru: ")
            if not nama_tugas:
                print("Nama tugas tidak boleh kosong!")
                continue
            
            if nama_tugas in todo_list:
                print(f"Tugas '{nama_tugas}' sudah ada di dalam daftar.")
            else:
                # Status awal default adalah "Belum Selesai"
                todo_list[nama_tugas] = "Belum Selesai"
                print(f"Berhasil menambahkan tugas: '{nama_tugas}'")

        elif pilihan == '2':
            # 2. Tampilkan Semua Tugas
            if not todo_list:
                print("\nDaftar tugas masih kosong.")
            else:
                print("\n--- DAFTAR TUGAS ---")
                for index, (tugas, status) in enumerate(todo_list.items(), 1):
                    print(f"{index}. [{status}] {tugas}")

        elif pilihan == '3':
            # 3. Tandai Tugas Selesai
            if not todo_list:
                print("\nDaftar tugas kosong.")
                continue
            
            nama_tugas = input("Masukkan nama tugas yang ingin ditandai selesai: ")
            
            # Cek apakah tugas ada di dalam dictionary untuk mencegah error
            if nama_tugas in todo_list:
                if todo_list[nama_tugas] == "Selesai":
                    print(f"Tugas '{nama_tugas}' sebelumnya sudah berstatus Selesai.")
                else:
                    todo_list[nama_tugas] = "Selesai"
                    print(f"Tugas '{nama_tugas}' berhasil ditandai sebagai Selesai.")
            else:
                print(f"Error: Tugas '{nama_tugas}' tidak ditemukan di dalam daftar.")

        elif pilihan == '4':
            # 4. Hapus Tugas
            if not todo_list:
                print("\nDaftar tugas kosong.")
                continue
            
            nama_tugas = input("Masukkan nama tugas yang ingin dihapus: ")
            
            # Cek apakah tugas ada di dalam dictionary untuk mencegah error (KeyError)
            if nama_tugas in todo_list:
                del todo_list[nama_tugas]
                print(f"Tugas '{nama_tugas}' berhasil dihapus.")
            else:
                print(f"Error: Tugas '{nama_tugas}' tidak ditemukan di dalam daftar.")

        elif pilihan == '5':
            # 5. Tampilkan Jumlah Tugas Selesai dan Belum
            if not todo_list:
                print("\nDaftar tugas kosong.")
            else:
                # Menghitung jumlah berdasarkan value dalam dictionary
                jumlah_selesai = list(todo_list.values()).count("Selesai")
                jumlah_belum = list(todo_list.values()).count("Belum Selesai")
                
                print("\n--- STATISTIK TUGAS ---")
                print(f"- Total Tugas      : {len(todo_list)}")
                print(f"- Sudah Selesai    : {jumlah_selesai}")
                print(f"- Belum Selesai    : {jumlah_belum}")

        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan aplikasi To-Do List!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 6.")

if __name__ == "__main__":
    main()