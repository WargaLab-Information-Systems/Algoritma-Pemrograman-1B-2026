# soal no 3
suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

print("Suhu reaktor: ", suhu, "Celcius")
print("Tekanan gas: ", tekanan, "Bar")

if suhu > 1000:
    if tekanan > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu > 500: 
    if tekanan > 30:
        print("Tekanan tidak stabil")
    else:
        print("Operasi reaktor normal")
else:
    print("Reaktor belum cukup panas")


status = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("Status operasional: ", status)