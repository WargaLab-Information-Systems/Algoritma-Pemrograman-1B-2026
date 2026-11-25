print("Masukkan kode (3 digit)")

kode = int(input())
d1 = float(kode) / 100
d2 = float(kode) / 10 % 10
d3 = kode % 10

print("Nilai d1= " + str(d1))
print("Nilai d2= " + str(d2))
print("Nilai d3= " + str(d3))

pelacak = d1 * d3
if d2 % 2 == 1:
    pelacak = pelacak + 25
else:
    pelacak = pelacak - d2

print("Nilai pelacak " + str(pelacak))

if pelacak > 50:
    print("Kategori A")
else:
    if pelacak > 20:
        print("Kategori B")
    else:
        print("Password Ditolak")
        
if pelacak % 2 == 0:
    print("Siklus Genap")
else:
    print("Siklus Ganjil")
