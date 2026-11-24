# Input data
suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# Menentukan status bahaya reaktor
if suhu > 1000:
    if tekanan <= 50:
        status = "Bahaya Suhu. Segera Turun!"
    else:
        status = "MELTDOWN! SEGERA EVAKUASI!"

elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"

else:
    status = "Reaktor lumayan Panas"

# Menentukan status pompa
if suhu > 800:
    pompa = "Pompa Maksimal"
else:
    pompa = "Pompa Normal"

# Menampilkan hasil
print("\n=== STATUS REAKTOR ===")
print("Suhu :", suhu, "°C")
print("Tekanan :", tekanan, "Bar")
print("Status Bahaya :", status)
print("Status Pompa :", pompa)