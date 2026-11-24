baris_lampu = int(input("masukkan jumlah baris lampu: "))
per_baris = int(input("masukkan jumlah lampu pada baris ke-{baris}: "))

for i in range(1, baris_lampu + 1):
    print(f"baris_lampu {i}")
    for j in range(1, per_baris + 1):
        if j % 3 == 0:
            print("lampu mengalami gangguan")
        else:
            print("lampu berfungsi dengan normal")

    print("periksa sumber listrik utama taman")