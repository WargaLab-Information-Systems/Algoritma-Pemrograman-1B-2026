n = int(input("Masukkan bilangan bulat positif n: "))
while n <= 0:
    print("Nilai n harus lebih dari 0, silakan masukkan ulang!")
    n = int(input("Masukkan bilangan bulat positif n: "))

jarak = 3
print()

for i in range(1, n + 1):

    for j in range(n - i):
        print(' ', end=' ')

    for k in range(1, i + 1):
        print(i - k + 1, end=' ')

    for s in range(jarak):
        print(' ', end=' ')

    for k in range(1, i + 1):
        print(k, end=' ')

    print()