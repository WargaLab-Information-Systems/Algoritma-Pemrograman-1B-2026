#soal no 2
total = int(input("Masukkan total belanjaan: "))

if total % 100000 == 0:
    bayar = 0
    print("Selamat! Belanjaan Anda gratis")
elif total % 50000 == 0: 
    bayar = total - (total * 50/100)
    print("Diskon 50%")
elif total % 10000 == 0:
    bayar = total - (total * 20/100)
elif total >= 20000:
    bayar = total - (total * 10/100)
else:
    bayar = total 

print("Total akhir belanjaan Anda Rp.", bayar)

status = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin:", status)