regular = 40000
vip = 75000
vvip = 100000

total_pembelian = 0
# pelanggan = input("Masukkan jenis tiket: ")
# total = int(input("Masukkan jumlah tiket: "))
while True:
    pelanggan = input("Masukkan jenis tiket : ")
    total = int(input("Masukkan jumlah tiket: "))

    total +1
    if total == 0:
        break

    if pelanggan == ("regular"):
        tambah = input("apakah mau tambah minuman seharga 10.000/tiket? (Y?N)")
        if tambah == ("Y" and "y"):
            print("Anda menambah minuman seharga Rp. 10.000")
        else:
            print("Anda tidak menambah minuman") 

    if pelanggan == vip and vvip:
        print("Anda mendapatkan minuman gratis ")     



if pelanggan == ("regular"):
        tambah = input("apakah mau tambah minuman seharga 10.000/tiket? (Y?N)")
        if tambah == ("Y" and "y"):
            print("Anda menambah minuman seharga Rp. 10.000")
        else:
            print("Anda tidak menambah minuman") 

if pelanggan == vip and vvip:
      print("Anda mendapatkan minuman gratis ")         


if total > 3:
    member = input("Apakah mempunyai member card? (Y/N): ")
    if pelanggan == ("Y"):
        total_pembelian * 0.15
        print("Anda mendapatkan diskon 15%")
    else: 
        total_pembelian * 0.10
        print("Anda mendapatkan diskon 10%")

