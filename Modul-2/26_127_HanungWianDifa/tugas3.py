# Program Monitoring Reaktor Chernobyl

suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("\nSuhu reaktor  :", suhu, "°C")
print("Tekanan gas  :", tekanan, "Bar")

# Menentukan status bahaya reaktor
if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu. Segera Turunkan Daya!"
        
elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"

else:
    status = "Reaktor Belum Cukup Panas"

print("Status Reaktor :", status)

# Ternary operator untuk status pompa
status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("Status Pompa   :", status_pompa)