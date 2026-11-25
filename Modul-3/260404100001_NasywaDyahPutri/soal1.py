jumlah = 0 
total_pendapatan = 0
total_jarak = 0 
terjauh = 0 

while True: 
    jarak = int(input("Masukkan jarak (km), 0 untuk selesai: "))
    if jarak == 0:
        break
    if jarak < 0:
        print("Tidak Valid")
        continue

    jumlah += 1
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000 #jarak - 5 menghitung jarak tambahan karena 5km pertama udh ada
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlah % 5 == 0:
        tarif = tarif * 0.5
        print("Penumpang ke-%d mendapakan diskon 50%%" % jumlah)

    print("Tarif: Rp.", tarif)
    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > terjauh:
        terjauh = jarak


print("Jumlah penumpang :", jumlah)
print(f"Total pendapatan : Rp", total_pendapatan)
if jumlah > 0:
    print("Jarak terjauh    :", terjauh, "km")
    print(f"Rata-rata jarak  : {total_jarak / jumlah:.2f} km")
else:
    print("Belum ada penumpang.")