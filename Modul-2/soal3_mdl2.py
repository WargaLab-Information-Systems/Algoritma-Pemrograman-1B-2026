suhu = float(input("Masukkan suhu reaktor : "))
tekanan = float(input("Masukkan tekanan gas : "))

print("\n=== MONITORING REAKTOR ===")
print(f"Suhu Reaktor : {suhu} °C")
print(f"Tekanan Gas  : {tekanan} Bar")

# Pengondisian bersarang (nested if)
if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

# Ternary operator
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# Output hasil
print(f"Status Bahaya : {status}")
print(f"Status Pompa  : {pompa}")
