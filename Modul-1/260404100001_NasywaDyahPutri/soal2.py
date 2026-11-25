# Rumus: V = (1/3) * pi * r^2 * t
#soal 2
jari_jari = float(input("Masukkan jari-jari alas kerucut (cm): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))
pi = 22/7

volume = (1 / 3) * pi * (jari_jari ** 2) * tinggi

print(f"\nJari-jari alas : {jari_jari} cm")
print(f"Tinggi kerucut : {tinggi} cm")
print(f"Volume kerucut : {volume} cm^3")