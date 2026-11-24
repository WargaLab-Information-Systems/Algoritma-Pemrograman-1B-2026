data_pc = []
jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    data_pc.append([nama, status, ram])

print("\nHasil Evaluasi:")

def evaluasi_pc(status, ram):
    ram = int(ram)
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"
    
for pc in data_pc:
    try:
        hasil = evaluasi_pc(pc[1], pc[2])

    except ValueError:
        hasil = "Format RAM Kacau"

    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')