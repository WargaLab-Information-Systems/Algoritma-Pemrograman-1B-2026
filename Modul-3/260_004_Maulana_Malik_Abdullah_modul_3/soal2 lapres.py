while True:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))
    if 2 <= n <= 15:
        break
    print("Input tidak valid, ulangi!")

baris = list(range(1, n + 1)) + list(range(n - 1, 0, -1))

for i in baris:
    spasi = " " * (n - i)                              
    naik  = "".join(str(j % 10) for j in range(1, i + 1))   # 1 sampai i
    turun = "".join(str(j % 10) for j in range(i - 1, 0, -1))  # i-1 sampai 1
    print(spasi + naik + turun)