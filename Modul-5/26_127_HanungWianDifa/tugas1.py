
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input jumlah hari
N = int(input("Masukkan hari ke-N: "))

# Validasi input
while N <= 0:
    print("Input harus berupa bilangan bulat positif!")
    N = int(input("Masukkan kembali hari ke-N: "))

# Menampilkan hasil
print("Jumlah pelanggan pada hari ke-", N, "adalah", fibonacci(N), "orang")
