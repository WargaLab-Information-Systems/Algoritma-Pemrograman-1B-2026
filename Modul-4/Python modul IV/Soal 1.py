baris = int(input("Masukkan jumlah baris lampu: "))
jumlah = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print(f"\nPemeriksaan baris ke-{i}")

    for j in range(1, jumlah + 1):
        if j % 3 == 0:
            print(f"Lampu ke-{j}: Mengalami gangguan")
        else:
            print(f"Lampu ke-{j}: Berfungsi normal")
            print("\nPeriksa sumber listrik utama taman!")  