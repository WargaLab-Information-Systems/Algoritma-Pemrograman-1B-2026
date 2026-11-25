penuh = 0

for i in range(10):
    print(f"\nMahasiswa ke-{i + 1}")
    nama = input("Nama                   : ")
    ipk = float(input("IPK (pakai titik)     : "))
    penghasilan = int(input("Penghasilan orang tua : "))

    if ipk < 3.00:
        print(f"{nama}: Tidak memenuhi syarat (IPK < 3,00)")
        continue                       # lewati ke mahasiswa berikutnya

    if penghasilan <= 3000000:
        print(f"{nama}: Beasiswa PENUH")
        penuh += 1
    elif penghasilan <= 5000000:
        print(f"{nama}: Beasiswa SEBAGIAN")
    else:
        print(f"{nama}: Tidak mendapat beasiswa")

    if penuh == 3:
        print("\nKuota beasiswa penuh (3 mahasiswa) terpenuhi. Seleksi dihentikan.")
        break                          # hentikan seluruh proses

print("\nSeleksi selesai. Beasiswa penuh diberikan kepada", penuh, "mahasiswa.")