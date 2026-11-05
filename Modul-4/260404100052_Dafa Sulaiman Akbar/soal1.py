jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))
print()

for baris in range(1, jumlah_baris + 1):
    print(f"Baris {baris}")

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"  Lampu {lampu} : mengalami gangguan")
        else:
            print(f"  Lampu {lampu} : berfungsi normal")

print()
print("Pemeriksaan selesai. Silakan periksa sumber listrik utama taman.")