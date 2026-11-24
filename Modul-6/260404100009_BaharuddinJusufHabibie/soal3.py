ram_minimal = 8
status_layak = "Layak"
status_tidak_layak = "Tidak Layak"
status_ram_kacau = "Format RAM Kacau"


def baca_jumlah_pc():
    # Jumlah PC harus bilangan bulat positif; ulangi sampai valid.
    while True:
        try:
            jumlah = int(input("Masukkan jumlah PC yang akan didata: "))
            if jumlah > 0:
                return jumlah
            print("Jumlah harus lebih dari 0.")
        except ValueError:
            print("Jumlah harus berupa angka bulat.")


def input_inventaris(jumlah):
    # Mengisi list 2D [nama, status, ram]. RAM sengaja disimpan apa adanya (tanpa validasi).
    inventaris = []
    for i in range(1, jumlah + 1):
        print(f"\nData PC ke-{i}")
        nama = input("  Nama PC            : ")
        status = input("  Status (Normal/Rusak): ")
        ram = input("  Kapasitas RAM (GB) : ")
        inventaris.append([nama, status, ram])
    return inventaris


def evaluasi_kelayakan(pc):
    # Mengembalikan 'Layak' / 'Tidak Layak'.

    # RAM selalu dikonversi lebih dulu, sehingga data RAM yang kacau
    # memicu ValueError (ditangani oleh pemanggil), apa pun status PC-nya.
    ram = int(pc[2])
    status_normal = pc[1].strip().lower() == "normal"
    if status_normal and ram >= ram_minimal:
        return status_layak
    return status_tidak_layak


def cetak_hasil(inventaris):
    for pc in inventaris:
        try:
            kelayakan = evaluasi_kelayakan(pc)
        except ValueError:
            kelayakan = status_ram_kacau
        print('{ "PC": "' + pc[0] + '", "Status": "' + kelayakan + '" }')


def kelola_inventaris_pc():
    jumlah = baca_jumlah_pc()
    inventaris = input_inventaris(jumlah)
    print("\nHasil evaluasi:")
    cetak_hasil(inventaris)


kelola_inventaris_pc()