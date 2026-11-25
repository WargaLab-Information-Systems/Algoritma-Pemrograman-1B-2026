# Program statis: semua nilai ditulis langsung di kode (tanpa input)

# Data
jarak_sekali_jalan = 100   # km
konsumsi = 40              # km per liter
sisa_bensin = 1.5          # liter
harga_per_liter = 10000    # Rp

# Perhitungan
total_jarak = jarak_sekali_jalan * 2             # pulang-pergi
kebutuhan_bensin = total_jarak / konsumsi        # liter
bensin_dibeli = kebutuhan_bensin - sisa_bensin   # liter
total_biaya = bensin_dibeli * harga_per_liter    # Rp

# Output
print("Total jarak pulang-pergi :", total_jarak, "km")
print("Total kebutuhan bensin   :", kebutuhan_bensin, "liter")
print("Bensin yang harus dibeli :", bensin_dibeli, "liter")
print("Total biaya              : Rp", total_biaya)
