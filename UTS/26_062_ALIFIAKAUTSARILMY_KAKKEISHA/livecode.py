regular = 40000
vip = 75000
vvip = 100000
nominal_uang = 0

nominal_uang = int(input("masukkan jumalah uang anda: "))
if nominal_uang == 40000:
    print("selamat pembayaran tiket regular berhasil")
elif nominal_uang == 75000:
    print("selamat pembayaran tiket vip berhasil")
elif nominal_uang == 100000:
    print("selamat pembayaran tiket vvip berhasil")