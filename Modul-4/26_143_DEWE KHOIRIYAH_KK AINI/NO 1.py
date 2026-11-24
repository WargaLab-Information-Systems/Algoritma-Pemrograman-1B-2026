
baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for b in range(1, baris + 1):
    print(f"\nPemeriksaan baris ke-{b}")

    for l in range(1, jumlah_lampu + 1):
        if l % 3 == 0:
            print(f"Lampu {l}: Mengalami gangguan")
        else:
            print(f"Lampu {l}: Berfungsi normal")

print("\nPemeriksaan seluruh lampu selesai.")
print("Silakan periksa sumber listrik utama taman.")   