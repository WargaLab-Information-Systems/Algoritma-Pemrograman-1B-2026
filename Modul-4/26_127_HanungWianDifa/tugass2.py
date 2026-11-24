total_gaji = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    gaji_pokok = 100000

    while True: 
        lembur = int(input("Masukkan jam lembur (0-8): "))

        if lembur < 0 or lembur == 5 or lembur == 7 or lembur > 8:
            print("Jam lembur tidak sesuai ketentuan. Masukkan ulang!")
        else:
            break

    if lembur == 0:
        upah_lembur = 0
    elif 1 <= lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000

    shift = input("Apakah bekerja shift malam? (y/t): ").lower()

    if shift == "y":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    gaji_harian = gaji_pokok + upah_lembur + tambahan_shift
    total_gaji += gaji_harian

    print(f"Gaji pokok    : Rp{gaji_pokok:}")
    print(f"Upah lembur   : Rp{upah_lembur:}")
    print(f"Tambahan shift: Rp{tambahan_shift:}")
    print(f"Gaji hari ini : Rp{gaji_harian:}")
    print(f"total gaji    : Rp{total_gaji:}")