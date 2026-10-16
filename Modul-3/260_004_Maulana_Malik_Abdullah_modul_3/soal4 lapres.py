JUMLAH_MAHASISWA = 10
KUOTA_PENUH = 3
beasiswa_penuh = 0

for i in range(1, JUMLAH_MAHASISWA + 1):
    print(f"\n=== Mahasiswa ke-{i} ===")
    nama = input("Nama                      : ")
    ipk = float(input("IPK                       : "))
    penghasilan = int(input("Penghasilan orang tua/bln : Rp"))

    # Syarat IPK: jika tidak memenuhi, lewati mahasiswa ini
    if ipk < 3.00:
        print(f"{nama}: tidak memenuhi syarat (IPK < 3,00)")
        continue

    # Seleksi berdasarkan penghasilan orang tua
    if penghasilan <= 3000000:
        print(f"{nama}: mendapat BEASISWA PENUH")
        beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        print(f"{nama}: mendapat BEASISWA SEBAGIAN")
    else:
        print(f"{nama}: tidak mendapat beasiswa (penghasilan > Rp5.000.000)")

    # Hentikan proses jika kuota beasiswa penuh sudah terpenuhi
    if beasiswa_penuh == KUOTA_PENUH:
        print("\nKuota beasiswa penuh (3 mahasiswa) telah terpenuhi.")
        print("Proses seleksi dihentikan.")
        break

print(f"\nTotal penerima beasiswa penuh: {beasiswa_penuh} mahasiswa")