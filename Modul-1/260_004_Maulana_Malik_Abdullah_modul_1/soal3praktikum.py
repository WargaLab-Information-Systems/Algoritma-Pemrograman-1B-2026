# Data yang diketahui
jarak_sekali_jalan = 100      # km
konsumsi_bbm = 40             # km per liter
sisa_bbm = 1.5                # liter
harga_per_liter = 10000       # Rupiah

# Perhitungan
total_jarak = jarak_sekali_jalan * 2                  # pulang-pergi
total_kebutuhan_bbm = total_jarak / konsumsi_bbm      # liter
bbm_dibeli = max(total_kebutuhan_bbm - sisa_bbm, 0)   # liter yang harus dibeli
total_biaya = bbm_dibeli * harga_per_liter            # Rupiah

# Output
print("=== Perencanaan Perjalanan Dimas ===")
print(f"Total jarak pulang-pergi      : {total_jarak} km")
print(f"Total kebutuhan bahan bakar   : {total_kebutuhan_bbm} liter")
print(f"Sisa bahan bakar di tangki    : {sisa_bbm} liter")
print(f"Bahan bakar yang harus dibeli : {bbm_dibeli} liter")
print(f"Total biaya pembelian         : Rp{total_biaya:,.0f}")