def hitung_pelanggan(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return hitung_pelanggan(n - 1) + hitung_pelanggan(n - 2)

try:
    n = int(input("Masukkan hari ke-N: "))
    if n <= 0:
        print("Masukkan bilangan bulat positif (N > 0).")
    else:
        print("Jumlah pelanggan pada hari ke-", n, "adalah:", hitung_pelanggan(n))
except ValueError:
    print("Input tidak valid! Harap masukkan angka.")
