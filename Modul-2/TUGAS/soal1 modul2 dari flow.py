print("Masukkan kode rahasia 3 digit: ")
kode = int(input())
digit1 = int(float(kode) / 100)
digit2 = int(float(kode) / 10) % 10
digit3 = kode % 10
pelacakawal = digit1 * digit3
if digit2 % 2 == 1:
    pelacak1 = pelacakawal + 25
else:
    pelacak1 = pelacakawal - digit2
if pelacak1 % 3 == 0:
    pelacakakhir = int(float(pelacak1) / 3)
else:
    pelacakakhir = pelacak1 * 2
if pelacakakhir > 50:
    status = "Password Kategori A"
else:
    if pelacakakhir > 20:
        status = "Password Kategori B"
    else:
        status = "Password Ditolak"
if pelacakakhir % 2 == 0:
    siklus = "Siklus Genap"
else:
    siklus = "Siklus Ganjil"
print("Digit pertama: " + str(digit1))
print("Digit kedua: " + str(digit2))
print("Digit ketiga: " + str(digit3))
print("Nilai pelacak awal: " + str(pelacakawal))
print("Setelah perubahan tahap 1: " + str(pelacak1))
print("Setelah perubahan tahap 2 (nilai akhir): " + str(pelacakakhir))
print("Status: " + status)
print(siklus)
