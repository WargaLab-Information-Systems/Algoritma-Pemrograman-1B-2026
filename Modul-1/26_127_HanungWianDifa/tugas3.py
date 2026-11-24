
# Program Menghitung Kebutuhan Bensin Dimas

# Data yang diketahui
jarak = 100
konsumsi_bensin = 40
sisa_bensin = 1.5
harga_bensin = 10000

# Menghitung total jarak pulang-pergi
total_jarak = jarak * 2

# Menghitung total kebutuhan bensin
total_bensin = total_jarak / konsumsi_bensin

# Menghitung bensin yang harus dibeli
bensin_dibeli = total_bensin - sisa_bensin

# Menghitung total biaya bensin
total_biaya = bensin_dibeli * harga_bensin

# Menampilkan hasil
print("HASIL PERHITUNGAN PERJALANAN DIMAS")
print("Total jarak pulang-pergi :", total_jarak, "km")
print("Total kebutuhan bensin   :", total_bensin, "liter")
print("Bensin yang harus dibeli :", bensin_dibeli, "liter")
print("Total biaya bensin       : Rp", total_biaya)





nomor_acarak = 7 

print("tebakvnomor acah dri 1-10")
tebakan = int (input("tebakan anda(bilangn bulat):)"))

if tebakan == nomor_acarak:
    print("selamat tebakan anda benar")
    print("tapi tidak ada hadiah untuk anda")
