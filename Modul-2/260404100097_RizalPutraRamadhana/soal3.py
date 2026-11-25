suhu = int(input("Masukan suhu: "))
tekanan = int(input("Masukan tekanan: "))

if suhu > 1000:
    if tekanan > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu > 500:
    if tekanan > 30:
        print("Tekanan Tidak Stabil")
    else:
        print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")

if suhu > 800:
    print("Pompa Air")
else:
    print("Pompa Normal")


print(suhu)
print(tekanan)