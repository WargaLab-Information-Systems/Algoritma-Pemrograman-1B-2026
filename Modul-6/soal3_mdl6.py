def evaluasi_pc(data_pc):
    ram = int(data_pc[2])

    if data_pc[1].lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print(f"\nData PC ke-{i+1}")

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    inventaris.append([nama, status, ram])

print("\n--- HASIL EVALUASI INVENTARIS PC ---")

for pc in inventaris:
    try:
        hasil = evaluasi_pc(pc)
    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'
    print(output)