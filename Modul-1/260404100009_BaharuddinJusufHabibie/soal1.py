uang = 200000
jumlah_buku = 3
harga_buku = 25000
jumlah_pulpen = 2
harga_pulpen = 8000
jumlah_flashdisk = 1
harga_flashdisk = 75000
 
total_buku = jumlah_buku * harga_buku
total_pulpen = jumlah_pulpen * harga_pulpen
total_flashdisk = jumlah_flashdisk * harga_flashdisk
total_belanja = total_buku + total_pulpen + total_flashdisk
 
diskon = total_belanja * 0.10
setelah_diskon = total_belanja - diskon
pajak = setelah_diskon * 0.11
total_bayar = setelah_diskon + pajak
kembalian = uang - total_bayar
 
print("a) Total harga buku: Rp" + str(total_buku))
print("b) Total harga pulpen: Rp" + str(total_pulpen))
print("c) Total harga flashdisk: Rp" + str(total_flashdisk))
print("d) Total sebelum diskon: Rp" + str(total_belanja))
print("e) Diskon 10%: Rp" + str(diskon))
print("f) Harga setelah diskon: Rp" + str(setelah_diskon))
print("g) PPN 11%: Rp" + str(pajak))
print("h) Total pembayaran: Rp" + str(total_bayar))
 
if uang >= total_bayar:
    print("i) Uang kembalian: Rp" + str(kembalian))
else:
    print("Uang Udin kurang: Rp" + str(total_bayar - uang))