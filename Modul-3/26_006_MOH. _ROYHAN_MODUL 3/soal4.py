jumlah_beasiswa_penuh = 0

for i in range(1, 11):
    if jumlah_beasiswa_penuh >= 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        break

    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat karena IPK kurang dari 3.00.")
        continue
    penghasilan = float(input("Masukkan penghasilan orang tua per bulan: "))
    
    if penghasilan <= 3000000:
        status = "Beasiswa penuh"
        jumlah_beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"
    else:
        status = "Tidak mendapatkan beasiswa"

print("Nama:", nama)
print("IPK:", ipk)
print("Penghasilan orang tua: Rp", int(penghasilan))
print("Hasil seleksi:", status)
print("\nJumlah penerima beasiswa penuh:", jumlah_beasiswa_penuh)
print("Proses seleksi selesai.")