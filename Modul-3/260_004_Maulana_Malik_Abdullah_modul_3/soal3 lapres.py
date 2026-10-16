nama_list, akhir_list, kategori_list = [], [], []
jumlah = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

for i in range(10):
    nama  = input("Nama  : ")
    tugas = float(input("Tugas : "))
    uts   = float(input("UTS   : "))
    uas   = float(input("UAS   : "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        kat = "A"
    elif akhir >= 75:
        kat = "B"
    elif akhir >= 65:
        kat = "C"
    elif akhir >= 50:
        kat = "D"
    else:
        kat = "E"

    jumlah[kat] += 1
    nama_list.append(nama)
    akhir_list.append(akhir)
    kategori_list.append(kat)

    print(f"{nama} | Tugas {tugas} | UTS {uts} | UAS {uas} | Akhir {akhir:.2f} | {kat}\n")

print("Jumlah per kategori:", jumlah)

tinggi = max(akhir_list)
rendah = min(akhir_list)
print("Tertinggi:", round(tinggi, 1), "-", nama_list[akhir_list.index(tinggi)])
print("Terendah :", round(rendah, 1), "-", nama_list[akhir_list.index(rendah)])
print("Rata-rata:", sum(akhir_list) / 10)