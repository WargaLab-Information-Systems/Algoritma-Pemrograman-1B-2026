jarak_sekali_jalan = 100
konsumsi_bbm = 40
sisa_bensin = 1.5
harga_bbm = 10000

total_jarak = jarak_sekali_jalan * 2

total_kebutuhan_bbm = total_jarak / konsumsi_bbm

bbm_harus_dibeli = total_kebutuhan_bbm - sisa_bensin

total_biaya = bbm_harus_dibeli * harga_bbm

print("=== Rencana Perjalanan Dimas ===")
print(f"Total jarak pulang-pergi        : {total_jarak} km")
print(f"Total kebutuhan bahan bakar     : {total_kebutuhan_bbm} liter")
print(f"Bahan bakar yang harus dibeli   : {bbm_harus_dibeli} liter")
print(f"Total biaya bahan bakar         : Rp{total_biaya:,.0f}")