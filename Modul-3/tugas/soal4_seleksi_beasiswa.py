# SOAL 4 - Seleksi Awal Penerima Beasiswa

beasiswa_penuh = 0
diproses = 0

print("=== SELEKSI BEASISWA ===")

for i in range(1, 11):
    print("--- Mahasiswa ke-%d ---" % i)
    nama = input("Nama                      : ")
    ipk = float(input("IPK (pakai titik, 3.50)  : "))
    penghasilan = int(input("Penghasilan orang tua/bln: Rp"))

    diproses += 1

    # IPK tidak memenuhi -> lewati, lanjut ke mahasiswa berikutnya
    if ipk < 3.00:
        print("Hasil:", nama, "TIDAK MEMENUHI SYARAT (IPK < 3,00)")
        continue

    if penghasilan <= 3000000:
        print("Hasil:", nama, "mendapat BEASISWA PENUH")
        beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        print("Hasil:", nama, "mendapat BEASISWA SEBAGIAN")
    else:
        print("Hasil:", nama, "TIDAK mendapat beasiswa")

    # Kuota penuh -> hentikan seluruh proses
    if beasiswa_penuh == 3:
        print("Kuota beasiswa penuh (3 orang) sudah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

print("=== RINGKASAN ===")
print("Mahasiswa diproses     :", diproses)
print("Penerima beasiswa penuh:", beasiswa_penuh)
