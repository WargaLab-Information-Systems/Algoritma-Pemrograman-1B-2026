
# Membuat list multidimensi
inventaris = []

# Input jumlah PC
jumlah = int(input("Masukkan jumlah PC: "))

# Input data PC
for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    inventaris.append([nama, status, ram])

# Fungsi untuk mengevaluasi PC
def evaluasi(pc):
    ram = int(pc[2])

    if pc[1] == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

# Menampilkan hasil evaluasi
print("\nHasil Evaluasi Inventaris PC:")

for pc in inventaris:
    try:
        hasil = evaluasi(pc)

    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    # Membuat output menggunakan manipulasi string
    output = '{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }'

    print(output)
