# Soal 1
password = int(input("Masukkan 3 digit password: "))

digit1 = password // 100
digit2 = (password // 10) % 10
digit3 = password % 10

print("Digit pertama:", digit1)
print("Digit kedua:", digit2)
print("Digit ketiga:", digit3)

nilai_pelacak_awal = digit1 * digit3
print("Nilai pelacak awal:", nilai_pelacak_awal)

if digit2 % 2 == 1:
    nilai_pelacak_tahap1 = nilai_pelacak_awal + 25
else:
    nilai_pelacak_tahap1 = nilai_pelacak_awal - digit2

print("Nilai pelacak setelah tahap pertama:", nilai_pelacak_tahap1)

if nilai_pelacak_tahap1 % 3 == 0:
    nilai_akhir = nilai_pelacak_tahap1 // 3
else:
    nilai_akhir = nilai_pelacak_tahap1 * 2

print("Nilai pelacak setelah tahap kedua (nilai akhir):", nilai_akhir)

if nilai_akhir > 50:
    status = "Kategori A"
elif nilai_akhir > 20:
    status = "Kategori B"
else:
    status = "Password Ditolak"

print("Status Password:", status)

if nilai_akhir % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")