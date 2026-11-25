
# gaji harian karyawan

total_gaji = 0
for hari in range(1, 8):
    print(f"\n hari ke {hari}")

    gaji_pokok = 100.000

    while True:
        jam_lembur = int(input("masukkan jam lembur (0-4,6, atau 8): "))

        if jam_lembur in [0, 1, 2, 3, 4, 6, 8]:
            break
        else:
            print("jam_lembur tidak sesuai dengan ketentuan. masukkan ulang!")

    if jam_lembur <= 3:
        gaji_lembur = jam_lembur * 25.000
    elif jam_lembur == 4:
        gaji_lembur = jam_lembur * 100.000
    elif jam_lembur == 6:
        gaji_lembur = 200.000
    else:
        gaji_lembur = 300.000

    shift = input(" apakah Bekerja shift malam? (ya/tidak): ")

    if shift == "ya":
        tambahan_malam = 50.000
    else:
        tambahan_malam = 0

    gaji_harian = gaji_pokok + gaji_lembur + tambahan_malam
    total_gaji += gaji_harian

    print(f"gaji hari ke-{hari}: Rp:{gaji_harian:,}")

print(f"\ntotal gaji selama 7 hari: Rp{total_gaji:,}")

