suhu = float(input("Masukkan suhu reaktor (Celsius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("\n=== HASIL PEMERIKSAAN ===")
print("Suhu :", suhu, "C")
print("Tekanan :", tekanan, "Bar")

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Suhu terlalu tinggi! Periksa sistem pendingin!"

elif suhu > 500:
    if tekanan > 30:
        status ="tekanan tidak stabil"
    else:
        status = "Suhu tinggi, monitor terus!"

else:
    status = "reaktor belum cukup panas, aman untuk operasi normal."

print("Status :", status)
status_reaktor = "Kondisi kritis!" if suhu > 1000 and tekanan > 50
else "Kondisi aman."
print("Status reaktor:", status_reaktor)