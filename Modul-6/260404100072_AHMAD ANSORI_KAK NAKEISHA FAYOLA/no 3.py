
data_pc = []

# Memasukkan jumlah PC
jumlah = int(input("Masukkan jumlah PC: "))

# Menginput data setiap PC
for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    data_pc.append([nama, status, ram])

# Melakukan evaluasi
print("=== HASIL EVALUASI PC ===")

for pc in data_pc:
    nama = pc[0]
    status = pc[1]
    ram = pc[2]

    try:
        kapasitas = int(ram)

        if status.lower() == "normal" and kapasitas >= 8:
            kelayakan = "Layak"
        else:
            kelayakan = "Tidak Layak"

    except ValueError:
        kelayakan = "Format RAM Kacau"

    # Membuat format menggunakan manipulasi string
    hasil = '{"PC": "' + nama + '", "Status": "' + kelayakan + '"}'

    print(hasil)