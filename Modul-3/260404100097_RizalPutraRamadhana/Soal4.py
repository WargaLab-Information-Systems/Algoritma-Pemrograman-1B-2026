jumlah_mahasiswa_penuh = 0

for mahasiswa in range(1,11):
    nama = input("masukkan nama = ")
    ipk = float(input("masukkan IPK = "))
    penghasilan_ortu = int(input("masukkan nominal pendatapan orang tua = "))
    if ipk < 3.00:
        print("tidak memenuhi")
    else:
        if ipk >= 3.00:
            print("memenuhi syarat")
            if penghasilan_ortu <= 3000000:
                print("mendapatkan beasiswa penuh")
                jumlah_mahasiswa_penuh += 1
            elif penghasilan_ortu <= 5000000:
                print("mendapatkan beasiswa sebagian")
            else:
                print("mahasiswa tidak mendapatkan beasiswa")


    if jumlah_mahasiswa_penuh == 3:
        break