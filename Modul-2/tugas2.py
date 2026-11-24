# Program Diskon Supermarket Koperasi Ndeso

total_belanja = int(input("Masukkan total belanja: Rp"))

if total_belanja % 100000 == 0:
    total_bayar = 0
    diskon = 100

elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 0.5
    diskon = 50

elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 0.8
    diskon = 20

elif total_belanja >= 200000:
    total_bayar = total_belanja * 0.9
    diskon = 10

else:
    total_bayar = total_belanja
    diskon = 0

# Tampilkan hasil
print("Total belanja awal : Rp", total_belanja)
print("Diskon :", diskon, "%")
print("Total yang dibayar : Rp", total_bayar)

# Ternary operator untuk status poin
status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
print("Status poin :", status_poin)