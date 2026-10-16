# Program Monitoring Reaktor Chernobyl - Krasny

# Input data dari indikator
suhu = float(input("Masukkan suhu reaktor (Celcius): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# Menampilkan data yang diinputkan
print("\n=== DATA INDIKATOR ===")
print(f"Suhu reaktor : {suhu} Celcius")
print(f"Tekanan gas  : {tekanan} Bar")

# Penentuan status bahaya (percabangan bersarang)
print("\n=== STATUS REAKTOR ===")
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

# Status pompa air menggunakan ternary operator
status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"
print("\n=== STATUS POMPA AIR ===")
print(status_pompa)