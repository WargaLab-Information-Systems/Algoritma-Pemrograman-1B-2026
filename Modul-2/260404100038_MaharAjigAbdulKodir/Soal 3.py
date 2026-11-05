# Program Pemantauan Reaktor

# Input suhu dan tekanan
suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# Menampilkan input
print("\nSuhu reaktor:", suhu, "°C")
print("Tekanan gas:", tekanan, "Bar")

# Menentukan status bahaya
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

# Ternary operator untuk pompa air
pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

# Menampilkan hasil
print("Status:", status)
print("Status Pompa:", pompa)