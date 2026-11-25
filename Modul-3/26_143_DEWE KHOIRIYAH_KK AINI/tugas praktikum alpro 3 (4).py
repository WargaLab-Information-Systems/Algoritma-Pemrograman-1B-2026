penuh = 0

for i in range(10):
    print("Mahasiswa ke-", i + 1)

    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    penghasilan = int(input("Penghasilan orang tua: Rp "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat.")
        continue

    if penghasilan <= 3000000:
        print(nama, "mendapat Beasiswa Penuh")
        penuh += 1

        if penuh == 3:
            print("Kuota beasiswa penuh sudah terpenuhi.")
            break

    elif penghasilan <= 5000000:
        print(nama, "mendapat Beasiswa Sebagian")

    else:
        print(nama, "tidak mendapat beasiswa")