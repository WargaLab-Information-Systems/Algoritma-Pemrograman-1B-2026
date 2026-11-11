n = int(input("Masukkan nilai n (bilangan bulat positif): "))

for i in range(1, n + 1):
    left_str = ""
    for j in range(1, i + 1):
        left_str += str(j) + " "

    spasi = " " * ((n - i) * 4)
    
    right_str = ""
    for j in range(i, 0, -1):
        right_str += str(j) + " "
        
    print(left_str + spasi + right_str)