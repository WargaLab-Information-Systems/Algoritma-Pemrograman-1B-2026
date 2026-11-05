print("=== Program Menghitung Volume Kerucut ===")

r_input = input("Masukkan jari-jari alas (cm) [default 7] : ")
r = float(r_input) if r_input else 7

t_input = input("Masukkan tinggi kerucut (cm) [default 12]: ")
t = float(t_input) if t_input else 12

volume = (1/3) * (22/7) * (r**2) * t 

print("=== Hasil perhitungan volume kerucut ===") 
print(f"Jari-jari (r) : {r} cm")
print(f"Tinggi (t) : {t} cm")
print(f"Volume kerucut : {volume} cm")