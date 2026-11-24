
n = int(input("Masukkan bilangan bulat positif: "))

while n <= 0:
    print("Input harus berupa bilangan bulat positif!")
    n = int(input("Masukkan bilangan bulat positif: "))

for i in range(1, n + 1):

    for j in range(n - i):
        print( end="" "",)

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(2 * (n - i) + 1):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()