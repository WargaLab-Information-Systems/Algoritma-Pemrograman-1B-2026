# soal 2
while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))
    if 2 <= n <= 15:
        break
    print("Di luar rentang, ulangi!")

lebar = 2 * n - 1

def buat_baris(i):
    teks = ""
    for k in range(1, i + 1):        # naik 1..i
        teks += str(k % 10)
    for k in range(i - 1, 0, -1):    # turun i-1..1
        teks += str(k % 10)
    return teks

# def untuk buat baris for pertama untuk baris bagian kiri, for kedua yang kanan

for i in range(1, n + 1):            # bagian atas
    print(buat_baris(i).center(lebar))

for i in range(n - 1, 0, -1):        # bagian bawah
    print(buat_baris(i).center(lebar))