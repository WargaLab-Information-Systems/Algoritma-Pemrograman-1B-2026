total_gaji = 0
gaji_pokok_per_hari = 100000
tambahan_shift_malam = 50000

print("=== PROGRAM PENGHITUNGAN GAJI MINGGUAN KARYAWAN ===")

for hari in range(1, 8):
    print(f"\n--- Data Hari ke-{hari} ---")
    
    while True:
        try:
            jam_lembur = int(input("Masukkan jam lembur (0-8 jam): "))
            if jam_lembur < 0:
                print("Jam lembur tidak boleh kurang dari 0. Silakan masukkan ulang.")
            elif jam_lembur > 8:
                print("Jumlah lembur melebihi batas yang ditentukan (maksimal 8 jam). Silakan masukkan ulang.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka bulat.")

    upah_lembur = 0
    if 1 <= jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000

    while True:
        shift = input("Apakah bekerja pada shift malam? (y/n): ").strip().lower()
        if shift in ['y', 'n']:
            break
        print("Input salah. Masukkan 'y' untuk ya atau 'n' untuk tidak.")

    gaji_shift = tambahan_shift_malam if shift == 'y' else 0
    gaji_harian = gaji_pokok_per_hari + upah_lembur + gaji_shift
    total_gaji += gaji_harian

    print(f"Gaji hari ke-{hari}: Rp {gaji_harian:,}")

print(f"\n==========================================")
print(f"TOTAL GAJI MINGGUAN KARYAWAN: Rp {total_gaji:,}")
print(f"==========================================")
