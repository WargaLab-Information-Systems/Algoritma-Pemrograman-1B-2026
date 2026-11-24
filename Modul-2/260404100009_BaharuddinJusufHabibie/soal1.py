print("masukkan 3 digit angka = ")
pin = int(input())
digit1 = int(float(pin) // 100)
print("digit pertama adalah = " + str(digit1))
digit2 = int(float(pin) // 10) % 10
print("digit kedua adalah = " + str(digit2))
digit3 = pin % 10
print("digit ketiga adalah = " + str(digit3))
nilaipelacak = digit1 * digit3
print("nilai pelacak tahap pertama adalah = " + str(nilaipelacak))
print("perubahan nilai pelacak tahap pertama")
if digit2 % 2 == 0:
    print("dikurangi angka digit2 = " + str(nilaipelacak - digit2))
else:
    print("maka ditambah 25 = " + str(nilaipelacak + 25))
print("perubahan nilai pelacak tahap kedua")
if nilaipelacak % 3 == 0:
    print("maka dibagi 3 = " + str(float(nilaipelacak) / 3))
else:
    print("maka dikalikan 2 = " + str(nilaipelacak * 2))
if nilaipelacak > 50:
    print("maka nilai pelacak kategori A")
else:
    if nilaipelacak > 20:
        print("maka nilai pelacak kategori B")
    else:
        print("password ditolak")
if nilaipelacak % 2 == 0:
    print("nilai pelacak adalah genap")
else:
    print("nilai pelacak adalah ganjil")