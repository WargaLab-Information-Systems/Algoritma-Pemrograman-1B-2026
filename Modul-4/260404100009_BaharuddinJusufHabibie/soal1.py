jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu_per_baris = int(input("Masukkan jumlah lampu pada setiap baris: "))

for baris in range(1, jumlah_baris + 1):
    print(f"\n--- Memeriksa Baris {baris} ---")
    for lampu in range(1, jumlah_lampu_per_baris + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu}: Mengalami gangguan")
        else:
            print(f"Lampu ke-{lampu}: Berfungsi normal")

print("\nPemeriksaan selesai. Harap segera memeriksa sumber listrik utama taman.")
