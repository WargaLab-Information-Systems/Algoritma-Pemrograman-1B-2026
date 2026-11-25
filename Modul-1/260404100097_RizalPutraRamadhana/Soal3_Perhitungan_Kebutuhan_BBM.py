jarak = 100
konsumsi = 40
sisa_tangki = 1.5
harga = 10000

total_jarak = jarak * 2
total_bensin = total_jarak // konsumsi
bensin_dibeli = total_bensin - sisa_tangki
total_biaya = bensin_dibeli * harga

print("Total Jarak  :", total_jarak, "km")
print("Bensin Dibeli:", bensin_dibeli, "liter")
print("Total Bensin:", total_bensin, "liter")
print("Total Biaya  : Rp", total_biaya)