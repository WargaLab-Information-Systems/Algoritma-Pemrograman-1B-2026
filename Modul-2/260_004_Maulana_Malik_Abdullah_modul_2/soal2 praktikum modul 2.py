# Program Kasir Supermarket "KOPERASI NDESO"

# Input jumlah barang dan harga tiap barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

total_awal = 0
for i in range(1, jumlah_barang + 1):
    harga = int(input(f"Harga barang ke-{i} (Rp): "))
    jumlah = int(input(f"Jumlah barang ke-{i}: "))
    total_awal += harga * jumlah

# Seleksi diskon berurutan dari yang terbesar
if total_awal > 0 and total_awal % 100000 == 0:
    diskon = 100          
    keterangan = "Gratis"
elif total_awal % 50000 == 0 and total_awal > 0:
    diskon = 50
    keterangan = "Diskon 50%"
elif total_awal % 10000 == 0 and total_awal > 0:
    diskon = 20
    keterangan = "Diskon 20%"
elif total_awal >= 200000:
    diskon = 10
    keterangan = "Diskon 10%"
else:
    diskon = 0
    keterangan = "Tidak ada diskon"

# Hitung total akhir
total_akhir = total_awal - (total_awal * diskon // 100)

# Status poin dengan ternary operator
status_poin = "Poin Bertambah" if total_akhir > 0 else "Tidak Ada Poin"

# Output
print("\n===== STRUK BELANJA =====")
print(f"Total belanja awal : Rp{total_awal:,}".replace(",", "."))
print(f"Promo              : {keterangan}")
print(f"Total bayar        : Rp{total_akhir:,}".replace(",", "."))
print(f"Status poin        : {status_poin}")