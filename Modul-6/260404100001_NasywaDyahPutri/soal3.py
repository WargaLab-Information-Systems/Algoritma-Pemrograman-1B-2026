def evaluasi(status, ram):
    if status == "Normal" and int(ram) >= 8:
        return "Layak"
    return "Tidak Layak"

jumlah = int(input("Masukkan jumlah PC: "))

inventaris = []

for i in range(jumlah):
    print(f"Data PC ke-{i + 1}")
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

print("--- Hasil Evaluasi ---")
for data in inventaris:
    nama, status, ram = data
    try:
        hasil = evaluasi(status, ram)
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + nama + '", "Status": "' + hasil + '" }')