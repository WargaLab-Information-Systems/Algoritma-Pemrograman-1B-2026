n = int(input("Masukkan bilangan bulat positif: "))

for i in range(1, n + 1):

    # Spasi sebelum piramida pertama
    for j in range(n - i):
        print(" ", end="")

    # Piramida angka pertama
    for j in range(1, i + 1):
        print(j, end="")

    # Spasi di antara kedua piramida
    for j in range(2 * (n - i) + 1):
        print(" ", end="")

    # Piramida angka kedua (cermin)
    for j in range(i, 0, -1):
        print(j, end="")

    print()
