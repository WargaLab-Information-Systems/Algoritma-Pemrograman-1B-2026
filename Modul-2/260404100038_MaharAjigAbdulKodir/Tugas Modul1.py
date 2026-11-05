# Data barang
jumlah_buku = 3
harga_buku = 25000

jumlah_pulpen = 2
harga_pulpen = 8000

jumlah_flashdisk = 1
harga_flashdisk = 75000

# Menghitung total masing-masing barang
total_buku = jumlah_buku * harga_buku
total_pulpen = jumlah_pulpen * harga_pulpen
total_flashdisk = jumlah_flashdisk * harga_flashdisk

# Total sebelum diskon
total_belanja = total_buku + total_pulpen + total_flashdisk

# Diskon 10%
diskon = total_belanja * 10 / 100

# Harga setelah diskon
harga_setelah_diskon = total_belanja - diskon

# PPN 11%
pajak = harga_setelah_diskon * 11 / 100

# Total pembayaran
total_pembayaran = harga_setelah_diskon + pajak

# Uang yang dibayarkan
uang_dibayar = 200000

# Uang kembalian
kembalian = uang_dibayar - total_pembayaran

# Menampilkan hasil
print("=== STRUK BELANJA UDIN ===")
print("Total harga buku       : Rp", total_buku)
print("Total harga pulpen     : Rp", total_pulpen)
print("Total harga flashdisk  : Rp", total_flashdisk)
print("Total sebelum diskon   : Rp", total_belanja)
print("Diskon 10%             : Rp", diskon)
print("Setelah diskon         : Rp", harga_setelah_diskon)
print("PPN 11%                : Rp", pajak)
print("Total pembayaran       : Rp", total_pembayaran)
print("Uang dibayar           : Rp", uang_dibayar)
print("Uang kembalian         : Rp", kembalian)