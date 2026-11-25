total_gaji = 0
gaji_pokok = 100000

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    lembur = int(input("Masukkan jam lembur (0, 1-3, 4, 6, atau 8): "))

    while lembur not in [0, 1, 2, 3, 4, 6, 8]:
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur: "))

    if lembur > 8:
        print("Jumlah lembur melebihi batas yang ditentukan!")
        upah_lembur = 0
    elif 1 <= lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("Apakah bekerja shift malam? (ya/tidak): ").lower()

    if shift == "ya":
        upah_shift = 50000
    else:
        upah_shift = 0

    gaji_harian = gaji_pokok + upah_lembur + upah_shift
    total_gaji += gaji_harian

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}".replace(",", "."))

print("\nTotal gaji mingguan: Rp{}".format(
    format(total_gaji, ",").replace(",", ".")
))