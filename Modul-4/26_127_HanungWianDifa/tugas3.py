
n = int(input("Masukkan bilangan bulat positif: "))

while n <= 0:
    print("Input harus berupa bilangan bulat positif!")
    n = int(input("Masukkan kembali nilai n: "))

for i in range(1, n + 1):
    # Piramida angka pertama
    for j in range(1, i + 1):
        print(j, end="")

    # Jarak antara kedua piramida
    print(" " * (2 * (n - i) + 1), end="")

    # Piramida angka kedua (cermin)
    for j in range(i, 0, -1):
        print(j, end="")

    print()
