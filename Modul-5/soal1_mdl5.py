def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

hari = int(input("Masukkan hari ke-N: "))

if hari > 0:
    jumlah = fibonacci(hari)
    print("Jumlah pelanggan pada hari ke-", hari, "adalah", jumlah, "orang")
else:
    print("Masukkan bilangan bulat positif!")
