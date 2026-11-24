suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

if suhu > 1000:
    if tekanan > 50:
        peringatan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        peringatan = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        peringatan = "Tekanan Tidak Stabil"
    else:
        peringatan = "Operasi Reaktor Normal"
else:
    peringatan = "Reaktor Belum Cukup Panas"

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Suhu     :", suhu, "C")
print("Tekanan  :", tekanan, "Bar")
print("Status   :", peringatan)
print("Pompa    :", pompa)