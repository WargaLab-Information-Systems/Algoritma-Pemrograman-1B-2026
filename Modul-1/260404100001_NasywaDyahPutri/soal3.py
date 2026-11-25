#soal 3
jarak_satu_arah = 100
konsumsi_bbm = 40 #40 km per per liter
sisa_bensin = 1.5 #sisa bensin sebelum berangkat
harga_per_liter = 10000

total_jarak = jarak_satu_arah * 2
kebutuhan_bbm = total_jarak / konsumsi_bbm
bbm_yang_dibeli = kebutuhan_bbm - sisa_bensin
total_biaya = bbm_yang_dibeli * harga_per_liter

print(f"Total jarak PP = {total_jarak} km")
print(f"Total kebutuhan bbm = {kebutuhan_bbm} liter")
print(f"Sisa bensin = {sisa_bensin}")
print(f"Bahan bakar yang harus dibeli = {bbm_yang_dibeli}")
print(f"Total biaya = Rp.{total_biaya}")