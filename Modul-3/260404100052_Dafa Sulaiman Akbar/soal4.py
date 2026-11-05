penuh = 0

for i in range(1, 11):
    print("\nMahasiswa ke-", i)
    nama = input("Nama                      : ")
    ipk = float(input("IPK                       : "))
    gaji = int(input("Penghasilan orang tua/bln : "))

    if ipk < 3.00:
        print(nama, ": IPK < 3,00, tidak memenuhi syarat")
        continue

    if gaji <= 3000000:
        print(nama, ": Beasiswa Penuh")
        penuh += 1
    elif gaji <= 5000000:
        print(nama, ": Beasiswa Sebagian")
    else:
        print(nama, ": Tidak mendapat beasiswa")

    if penuh == 3:
        print("\nKuota beasiswa penuh (3 mahasiswa) sudah terpenuhi.")
        break

print("\nJumlah penerima beasiswa penuh:", penuh)