# Soal 2
total_belanja = int(input("Masukkan total belanja: "))

print("Total belanja awal:", total_belanja)

if total_belanja % 100000 == 0:
    total_bayar = 0
elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 0.5
elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 0.8
elif total_belanja >= 200000:
    total_bayar = total_belanja * 0.9
else:
    total_bayar = total_belanja

print("Total harga akhir yang harus dibayar:", total_bayar)

status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
print("Status poin keanggotaan:", status_poin)