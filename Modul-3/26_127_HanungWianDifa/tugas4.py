
jumlah_penuh = 0
jumlah_sebagian = 0
jumlah_tidak_dapat = 0
jumlah_tidak_memenuhi = 0

for i in range(1, 11):
    print(f"\n=== Seleksi mahasiswa ke-{i} ===")

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 0 or ipk > 4:
        print("IPK tidak valid!")
        print("Data mahasiswa dilewati.")
        jumlah_tidak_memenuhi += 1
        continue

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat IPK.")
        jumlah_tidak_memenuhi += 1
        continue

    penghasilan = float(
        input("Penghasilan orang tua per bulan (Rp): ")
    )

    if penghasilan < 0:
        print("Penghasilan tidak valid!")
        jumlah_tidak_memenuhi += 1
        continue

    if penghasilan <= 3000000:
        if jumlah_penuh < 3:
            jumlah_penuh += 1
            print(nama, "mendapatkan beasiswa penuh.")
        else:
            jumlah_tidak_dapat += 1
            print(nama, "tidak mendapatkan beasiswa karena kuota penuh.")

    elif penghasilan <= 5000000:
        jumlah_sebagian += 1
        print(nama, "mendapatkan beasiswa sebagian.")

    else:
        jumlah_tidak_dapat += 1
        print(nama, "tidak mendapatkan beasiswa.")

    if jumlah_penuh == 3:
        print("\nKuota beasiswa penuh telah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

print("\n=== HASIL AKHIR SELEKSI ===")
print("Penerima beasiswa penuh:", jumlah_penuh)
print("Penerima beasiswa sebagian:", jumlah_sebagian)
print("Tidak mendapatkan beasiswa:", jumlah_tidak_dapat)
print("Tidak memenuhi syarat / data dilewati:", jumlah_tidak_memenuhi)
