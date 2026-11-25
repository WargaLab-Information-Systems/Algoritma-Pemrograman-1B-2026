baris = int(input("Masukkan jumlah baris lampu: "))
per_baris = int(input("Masukkan jumlah lampu setiap baris: "))

for i in range(1, baris + 1):
    print(f"Baris {i}:")
    for j in range(1, per_baris + 1):
        if j % 3 == 0:
            print("Lampu mengalami gangguan")
        else:
            print("Lampu berfungsi normal")

    

print("Periksa sumber listrik utama taman.")