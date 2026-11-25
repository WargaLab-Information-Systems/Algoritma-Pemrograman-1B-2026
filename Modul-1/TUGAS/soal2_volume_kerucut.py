import math

# Input dari pengguna
r = float(input("Masukkan jari-jari alas (cm): "))
t = float(input("Masukkan tinggi kerucut (cm): "))

# Rumus volume kerucut: V = 1/3 * pi * r^2 * t
volume = (1 / 3) * math.pi * r ** 2 * t

print(f"Volume kerucut = {volume:.2f} cm^3")
