jarakTempuh = 100
konsumsiBBM = 40
sisaBensin = 1.5
hargaBensin = 10000
# total jarak tempuh
totalJarakTempuh = jarakTempuh * 2
# total kebutuhan bensin
totalBensin = totalJarakTempuh / konsumsiBBM
# bensin yang harus dibeli
bensinDibeli = totalBensin - sisaBensin
# total biaya
totalBiaya = bensinDibeli * hargaBensin

print("Total jarak:", totalJarakTempuh, "km")
print("Kebutuhan BBM:", totalBensin, "liter")
print("BBM yang dibeli:", bensinDibeli, "liter")
print("Total biaya: Rp", totalBiaya)