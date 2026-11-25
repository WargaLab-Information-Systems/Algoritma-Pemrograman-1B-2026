def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

N = int(input("Masukkan hari ke-N: "))

if N > 0:
    print("Jumlah pelanggan pada hari ke-", N, "adalah:", fibonacci(N))
else:
    print("Masukkan bilangan bulat positif!")
