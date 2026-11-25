jarak = 100
konsumsi = 40
bensin_tersedia = 1.5
harga_bensin = 10000

total_jarak = jarak*2
kebutuhan_bensin =  total_jarak/konsumsi
bensin_dibeli = kebutuhan_bensin-bensin_tersedia
total_biaya = bensin_dibeli*harga_bensin

print("total jarak perjalanan:",total_jarak, "km")
print("kebutuhan bensin:", kebutuhan_bensin, "liter")
print("bensin yang dibeli", bensin_dibeli, "liter")
print("total biaya:Rp", total_biaya)
