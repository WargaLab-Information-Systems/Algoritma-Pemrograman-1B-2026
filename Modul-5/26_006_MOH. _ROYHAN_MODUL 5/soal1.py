def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

hari = int(input("Masukkan hari ke-: "))

if hari > 0:
    print("Jumlah pelanggan hari ke-", hari, "adalah:",fibonacci(hari))
else:
    print("Masukkan angka positif!")