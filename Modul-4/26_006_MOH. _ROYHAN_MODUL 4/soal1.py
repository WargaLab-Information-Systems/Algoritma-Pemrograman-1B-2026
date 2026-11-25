baris_lampu = int(input("masukkan jumlah baris lampu: "))

for baris in range(1, baris_lampu + 1):
    jumlah_lampu = (int(input(f'masukkan jumlah lampu pada baris ke {baris}: ')))
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"baris {baris} lampu {lampu} mengalami gangguan")
        else:
            print(f"baris {baris} lampu {lampu} normal")
 
    print("periksa sumber listrik utama taman")