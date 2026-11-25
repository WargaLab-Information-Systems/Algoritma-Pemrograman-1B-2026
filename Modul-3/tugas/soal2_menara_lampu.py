# SOAL 2 - Menara Lampu Hias (belah ketupat angka)

n = int(input("Masukkan tinggi setengah menara (2-15): "))
while n < 2 or n > 15:
    print("Di luar rentang, silakan ulangi!")
    n = int(input("Masukkan tinggi setengah menara (2-15): "))

# k = urutan baris dari 1 sampai 2n-1
for k in range(1, 2 * n):
    # i = "nomor baris" yang menentukan angka puncak
    if k <= n:
        i = k
    else:
        i = 2 * n - k

    baris = ""

    # angka naik dari 1 sampai i
    for x in range(1, i + 1):
        baris = baris + str(x % 10) + " "

    # angka turun dari i-1 sampai 1
    for x in range(i - 1, 0, -1):
        baris = baris + str(x % 10) + " "

    # spasi di depan agar rata tengah
    print(" " * (2 * (n - i)) + baris)
