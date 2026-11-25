def evaluasi_pc(data):
    if int(data[2]) >= 8 and data[1].lower() == "normal":
        return "Layak"
    else:
        return "Tidak Layak"

inventaris = []
jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    
    inventaris.append([nama, status, ram])

print("\n=== HASIL EVALUASI PC ===")

for pc in inventaris:
    try:
        hasil = evaluasi_pc(pc)
    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'

    print(output)