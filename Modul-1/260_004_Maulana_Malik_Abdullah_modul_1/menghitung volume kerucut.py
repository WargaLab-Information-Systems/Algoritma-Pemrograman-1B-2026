#program menghitung volume kerucut
#Rumus V = 1/3 * math.pi * r**2 * t

import math

#data yang diketahui
r = 7 #jari-jari alas (cm)
t = 12 #tinggi kerucut (cm)

#menghitung volume
volume = (1/3) * math.pi * r**2 * t

import math

r = float(input("Masukkan jari-jari alas (cm): "))
t = float(input("Masukkan tinggi kerucut (cm): "))

volume = (1 / 3) * math.pi * r**2 * t

print(f"Volume kerucut = {volume:.2f} cm³")