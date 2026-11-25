total_belanja = int(input("Masukkan total belanja: Rp"))

# Logika diskon
if total_belanja % 100000 == 0 and total_belanja > 0:
    total_bayar = 0  # Gratis jika kelipatan 100.000
elif total_belanja % 50000 == 0:
    total_bayar = (total_belanja * 0.5)  # Diskon 50%
elif total_belanja % 10000 == 0:
    total_bayar = (total_belanja * 0.8)  # Diskon 20%
elif total_belanja >= 200000:
    total_bayar = (total_belanja * 0.9)  # Diskon 10%
else:
    total_belanja = total_belanja

# status_poin ="poin bertambah" if total_bayar > 0 else"tidak ada poin"

if total_bayar > 0 :
    status_poin = "poin bertambah"
else :
    status_poin = "tidak ada poin"

# Output
print(f"Total belanja awal : Rp{total_belanja:,}")
print(f"Total harga akhir  : Rp{total_bayar:,}")
print(f"Status poin        : {status_poin}")
