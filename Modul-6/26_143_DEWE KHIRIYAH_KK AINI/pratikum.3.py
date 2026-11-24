inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

# Memasukkan data PC
for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = int(input("Kapasitas RAM (GB): "))

    data = [nama, status, ram]
    inventaris.append(data)

# Menampilkan seluruh data
print("DAFTAR INVENTARIS PC")

for pc in inventaris:
    print("Nama:", pc[0])
    print("Status:", pc[1])
    print("RAM:", pc[2], "GB")

# Evaluasi kelayakan
print("HASIL EVALUASI PC")

for pc in inventaris:
    if pc[1].lower() == "normal" and pc[2] >= 8:
        print(pc[0], "LAYAK DIGUNAKAN")
    else:
        print(pc[0], "TIDAK LAYAK DIGUNAKAN")
