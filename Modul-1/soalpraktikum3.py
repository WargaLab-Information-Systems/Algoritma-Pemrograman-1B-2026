# SOALPRAKTIKUM_NOMER3
Jaraktempuh = 100

konsumsiBBM = 40
sisaBensin = 1.5 
hargaBensin = 10000

# total jarak tempuh
totalJarakTempuh = Jaraktempuh * 2
# total kebutuhan bensin
totalbensin = totalJarakTempuh / konsumsiBBM
# bensin yang harus dibeli
bensindibeli = totalbensin - sisaBensin
# total biaya
totalbiaya = bensindibeli* hargaBensin

print("Total Jarak:", totalJarakTempuh, "KM")
print("Total Kebutuhan BBM:", totalbensin, "Liter")
print("Total Bensin dibeli:", bensindibeli, "Liter")
print("Total Biaya: Rp.", totalbiaya)
