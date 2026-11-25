n = int(input("Masukkan bilangan bulat positif n: "))
jarak = 3

for i in range(1, n + 1):
    for naik in range(1, i + 1):
        print(naik, end=" ")
    for s in range((n - i) * 2 + jarak):
        print(" ", end=" ")
    for turun in range(i, 0, -1):
        print(turun, end=" ")
    print()