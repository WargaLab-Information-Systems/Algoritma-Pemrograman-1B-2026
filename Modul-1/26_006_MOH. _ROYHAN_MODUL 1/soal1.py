Uang = 200000
buku = 3
harga_buku =25000
pulpen = 2
harga_pulpen =8000
flashdisk = 1
harga_flashdisk = 75000

total_harga_buku = buku * harga_buku
total_harga_pulpen = pulpen * harga_pulpen
total_harga_flashdisk = flashdisk * harga_flashdisk
total_belanjaan = total_harga_buku + total_harga_pulpen + harga_flashdisk

diskon = total_belanjaan * 0.10
setelah_diskon = total_belanjaan - diskon
pajak = setelah_diskon * 0.11
total_bayar = setelah_diskon + pajak
kembalian = Uang - total_bayar
 
print("a) Total harga buku: Rp" + str(total_harga_buku))
print("b) Total harga pulpen: Rp" + str(total_harga_pulpen))
print("c) Total harga flashdisk: Rp" + str(total_harga_flashdisk))
print("d) Total sebelum diskon: Rp" + str(total_belanjaan))
print("e) Diskon 10%: Rp" + str(diskon))
print("f) Harga setelah diskon: Rp" + str(setelah_diskon))
print("g) PPN 11%: Rp" + str(pajak))
print("h) Total pembayaran: Rp" + str(total_bayar))
 
if Uang >= total_bayar:
    print("i) Uang kembalian: Rp" + str(kembalian))
else:
    print("Uang Udin kurang: Rp" + str(total_bayar - Uang))

