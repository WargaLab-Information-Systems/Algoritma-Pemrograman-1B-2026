print("   PROGRAM HITUNG VOLUME KERUCUT    ")

# r adalah jari-jari alas dan t adalah tinggi kerucut
r = float(input("Jari-jari (cm): "))
t = float(input("Tinggi (cm): "))

# Menggunakan 3.14 sebagai nilai Pi
volume = 1 / 3 * 3.14 * r ** 2 * t

print("Volume Kerucut :", volume, "cm³")