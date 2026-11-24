def pelanggan(n):
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b
n = int(input("Masukkan nilai n: "))
print("Jumlah pada hari ke-", n, "adalah:", pelanggan(n))
