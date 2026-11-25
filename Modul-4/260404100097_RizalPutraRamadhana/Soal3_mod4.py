n = int(input("Masukkan nilai n: "))

for i in range(1, n + 1):

    # Piramida kiri
    for j in range(1, i + 1):
        print(j, end="")

    # Spasi di tengah
    for j in range(1, 2 * (n - i) + 3):
        print(" ", end="")

    # Piramida kanan
    for j in range(i, 0, -1):
        print(j, end="")

    print()