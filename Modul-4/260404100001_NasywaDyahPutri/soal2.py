total = 0

for hari in range(1, 8):
    print(f"\n Hari ke-{hari}")

    while True:
        lembur = int(input("Masukkan jam lembur: "))
        if lembur < 0 or lembur in (5,7):
            print("Jam lembur tidak valid. Masukkan lagi")
        else:
            break

    malam = input("Apakah kamu shift malam? (y/t): ").lower()

    gaji = 100000

    if lembur <= 1 or lembur <= 3:
        gaji += lembur * 25000
    elif lembur == 4: 
        gaji += lembur * 100000
    elif lembur == 6:
        gaji += lembur * 200000
    elif lembur == 8:
        gaji += lembur * 300000
    elif lembur > 8:
        print("Lembur melebihi batas yang sudah ditentukan, upah lembut tidak dihitung")

    if malam == "y":
        gaji += 50000

    print(f"Gaji hari ke-{hari}: ",gaji)
    total += gaji

print("\nTotal gaji mingguan: ",total)