
total_gaji = 0

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")
    
    lembur = int(input("Masukkan jam lembur (0-8): "))

    while lembur < 0 or lembur > 8 or lembur == 5 or lembur == 7:
        print("Jam lembur tidak sesuai ketentuan!")
        lembur = int(input("Masukkan ulang jam lembur (0-8): "))

    shift = input("Bekerja shift malam? (ya/tidak): ").lower()

    gaji_pokok = 100000

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

    if shift == "ya":
        tambahan_malam = 50000
    else:
        tambahan_malam = 0

    gaji_harian = gaji_pokok + upah_lembur + tambahan_malam
    total_gaji += gaji_harian

    print(f"Gaji hari ini: Rp{gaji_harian:,}".replace(",", "."))

print("\nTotal gaji selama 7 hari: Rp" +
      format(total_gaji, ",").replace(",", "."))
