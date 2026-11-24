suhu = float(input("Masukkan suhu reaktor (°C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

if suhu > 1000:
    if tekanan > 50:
        pesan_status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan_status = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        pesan_status = "Tekanan Tidak Stabil"
    else:
        pesan_status = "Operasi Reaktor Normal"
else:
    pesan_status = "Reaktor Belum Cukup Panas"

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("=== LAPAN SISTEM PEMANTAUAN REAKTOR ===")
print(f"Suhu Reaktor   : {suhu} °C")
print(f"Tekanan Gas    : {tekanan} Bar")
print(f"Status Bahaya  : {pesan_status}")
print(f"Status Pompa   : {status_pompa}")