def evaluasi(pc):
    ram = int(pc[2])
    if pc[1].lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

jumlah = int(input("Masukkan jumlah PC: "))
inventaris = []
for i in range(jumlah):
    print(f"Data PC ke-{i + 1}")
    nama = input("  Nama PC           : ")
    status = input("  Status (Normal/Rusak): ")
    ram = input("  Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

print()
print("=== Hasil Evaluasi ===")
for pc in inventaris:
    try:
        hasil = evaluasi(pc)
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')