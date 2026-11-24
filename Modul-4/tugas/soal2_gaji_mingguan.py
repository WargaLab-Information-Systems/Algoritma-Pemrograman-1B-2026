
total_gaji = 0          

for hari in range(1, 8):
    print(f"Hari ke-{hari}")

    jam = int(input("  Jam lembur (0 jika tidak lembur): "))

    while jam < 0 or jam == 5 or jam == 7:
        print("  Jam lembur tidak sesuai ketentuan, masukkan ulang!")
        jam = int(input("  Jam lembur (0 jika tidak lembur): "))

    shift = input("  Shift malam? (y/t): ")
    while shift != "y" and shift != "t":
        print("  Jawab dengan y atau t, masukkan ulang!")
        shift = input("  Shift malam? (y/t): ")

    gaji_hari = 100000
    if jam >= 1 and jam <= 3:
        gaji_hari = gaji_hari + jam * 25000
    elif jam == 4:
        gaji_hari = gaji_hari + 100000
    elif jam == 6:
        gaji_hari = gaji_hari + 200000
    elif jam == 8:
        gaji_hari = gaji_hari + 300000
    elif jam > 8:
        print("  Jumlah lembur melebihi batas yang ditentukan, upah lembur tidak dihitung.")

    if shift == "y":
        gaji_hari = gaji_hari + 50000

    print(f"  Gaji hari ke-{hari}: Rp{gaji_hari}")
    total_gaji = total_gaji + gaji_hari

print(f"Total gaji mingguan: Rp{total_gaji}")
