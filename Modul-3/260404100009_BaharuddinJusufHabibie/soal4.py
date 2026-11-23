jumlah_penuh = 0
kuota_penuh = 3

for i in range(1, 11):
    print(f"\nMahasiswa ke-{i}")
    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    penghasilan = int(input("Penghasilan orang tua: Rp"))

    # IPK kurang lewati mahasiswa ini
    if ipk < 3.00:
        print("Hasil:", nama, "- Tidak memenuhi syarat (IPK < 3,00)")
        continue

    # IPK cukup, cek penghasilan
    if penghasilan <= 3000000:
        print("Hasil:", nama, "- Mendapat BEASISWA PENUH")
        jumlah_penuh = jumlah_penuh + 1
    elif penghasilan <= 5000000:
        print("Hasil:", nama, "- Mendapat BEASISWA SEBAGIAN")
    else:
        print("Hasil:", nama, "- Tidak mendapat beasiswa (penghasilan > Rp5.000.000)")

    if jumlah_penuh == kuota_penuh:
        print("\nKuota beasiswa penuh sudah terpenuhi. Seleksi dihentikan.")
        break

print("\nJumlah penerima beasiswa penuh:", jumlah_penuh)