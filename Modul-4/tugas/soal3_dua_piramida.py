

n = int(input("Masukkan bilangan bulat positif n: "))
jarak = 5    

for i in range(1, n + 1):

    for k in range(1, i + 1):
        print(k, end=' ')
    for j in range(n - i):
        print(' ', end=' ')

    for j in range(jarak):
        print(' ', end=' ')

    for j in range(n - i):
        print(' ', end=' ')
    for k in range(i, 0, -1):
        print(k, end=' ')

    print()
