Regular = 40000
Vip = 75000
Vvip = 100000

for i in range(1, 4):

    # memasukkan jenis tiket (regular, vip dan vvip)
    tiket = input("Masukkan Jenis Tiket: ")

    # pengkondisian tiket / filter tiket
    if tiket == "regular":
        hargaTiket = Regular
        print("harga tiket anda", Regular)
        minuman = input("apakah anda akan menambahkan minuman: Y/n ")
    elif tiket == "vip":
        hargaTiket = Vip
        print("harga tiket anda", Vip)
        print("anda mendapat minuman gratis!")
    elif tiket == "vvip":
        hargaTiket = Vvip
        print("harga tiket anda", Vvip)
        print("anda mendapat minuman gratis!")

    if tiket != "regular" or "vip" or "vvip":
        continue
    
