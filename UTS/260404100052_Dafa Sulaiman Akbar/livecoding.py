tiket_reguler=1
tiket_vip=2
tiket_vvip=3
harga=0
kembalian=0
beli=0
minuman=0

print("==PESAN TIKET==")
print("input 1 jika reguler")
print("input 2 jika vip")
print("input 3 vvip")

while True:
    beli=int(input("mau beli tiket apa : "))
    if beli==1:
        harga=40000
        print("membeli tiket reguler dengan harga Rp. 40.000")
        print("apakah mau membeli minum Rp. 10.000? Y/N")
    minuman=str(input("mau atau tidak Y/N? : "))
    if minuman=="y" :
        print("kamu membeli minuman seharga 10.000")
        continue
    elif beli==2:
        harga=75000
        print("membeli tiket vip dengan harga Rp. 75.000")
    elif beli==3:
        harga=100000
        print("membeli tiket vvip dengan harga Rp. 100.000")
    else:
       print ("tiket tidak valid")
    continue