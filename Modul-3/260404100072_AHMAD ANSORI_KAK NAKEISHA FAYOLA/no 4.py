kuota_penuh = 0

for i in range(10):
    print(f"\nData mahasiswa ke-{i + 1}")
    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat IPK.")
        continue

    penghasilan = float(input("Penghasilan orang tua per bulan (Rp): "))

    if penghasilan <= 3000000:
        if kuota_penuh < 3:
            print(nama, "mendapatkan beasiswa penuh.")
            kuota_penuh += 1
        else:
            print(nama, "tidak mendapatkan beasiswa penuh karena kuota habis.")
            break

    elif penghasilan <= 5000000:
        print(nama, "mendapatkan beasiswa sebagian.")

    else:
        print(nama, "tidak mendapatkan beasiswa.")

    if kuota_penuh == 3:
        print("Kuota beasiswa penuh telah terpenuhi.")
        break

print("\nJumlah penerima beasiswa penuh:", kuota_penuh)