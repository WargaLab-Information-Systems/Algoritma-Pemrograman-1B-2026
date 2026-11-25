# soal no 1
kode = int(input("Masukkan kode rahasia (3 digit): "))

d1 = kode // 100 #mengambil nilai ratusan dengan kode dibagi 100
d2 = (kode // 10) % 10 #mengambil nilai puluhan dgn kode dibagi 10 hasilnya di modulo 10
d3 = kode % 10 #mengambil nilai satuan dgn kode di modulo 10

print("Digit pertama: ", d1)
print("Digit kedua: ", d2)
print("Digit ketiga: ", d3)

nilai_pelacak_awal = d1 * d3
print("Nilai pelacak awal: ", nilai_pelacak_awal)

if d2 % 2 == 1: 
    nilai_pelacak = nilai_pelacak_awal + 25
else: 
    nilai_pelacak= nilai_pelacak_awal - d2
print("Nilai pelacak tahap 1: ", nilai_pelacak)

if nilai_pelacak % 3 == 0:
    nilai_pelacak = nilai_pelacak // 3
else:
    nilai_pelacak = nilai_pelacak * 2
print("Nilai pelacak tahap 2: ", nilai_pelacak)

if nilai_pelacak > 50:
    print("Status: Password adalah Kategori A")
elif nilai_pelacak > 20:
    print("Status: Password adalah kategori B")
else:
    print("Status: Password ditolak")


if nilai_pelacak % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")