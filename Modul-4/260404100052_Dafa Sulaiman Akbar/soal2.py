gaji_pokok = 100000
tambahan_malam = 50000
total_gaji = 0

for hari in range(1, 8):
    print(f"=== Hari ke-{hari} ===")

    while True:
        jam_lembur = int(input("Jam lembur : "))
        if jam_lembur < 0 or jam_lembur in (5, 7):
            print("Jam lembur tidak sesuai ketentuan, silakan masukkan ulang!")
        else:
            break

    while True:
        shift = input("Shift malam (y/t) : ").lower()
        if shift == "y" or shift == "t":
            break
        print("Input harus y atau t, silakan masukkan ulang!")

    if jam_lembur == 0:
        upah_lembur = 0
    elif jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0
        print("Jumlah lembur melebihi batas yang ditentukan, upah lembur tidak dihitung.")

    if shift == "y":
        upah_malam = tambahan_malam
    else:
        upah_malam = 0

    gaji_hari = gaji_pokok + upah_lembur + upah_malam
    total_gaji = total_gaji + gaji_hari

    print(f"Gaji hari ke-{hari} : Rp{gaji_hari}")
    print()

print(f"Total gaji mingguan : Rp{total_gaji}")