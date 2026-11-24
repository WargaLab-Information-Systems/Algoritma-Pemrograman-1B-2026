
import math

# Menginput jari-jari dan tinggi kerucut
r = float(input("Masukkan jari-jari kerucut (cm): "))
t = float(input("Masukkan tinggi kerucut (cm): "))

# Menghitung volume kerucut
volume = (1/3) * math.pi * (r ** 2) * t

# Menampilkan hasil
print("HASIL VOLUME KERUCUT")
print("Jari-jari :", r, "cm")
print("Tinggi    :", t, "cm")
print("Volume    :", round(volume, 2), "cm³")
