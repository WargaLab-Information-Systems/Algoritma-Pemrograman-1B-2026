total_belanja = int(input("Masukkan total belanja awal (Rp): "))

if total_belanja % 100000 == 0:
    total_bayar = 0
    keterangan_diskon = "Gratis Total (Diskon 100%)"
elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 0.5
    keterangan_diskon = "Diskon 50%"
elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 0.8
    keterangan_diskon = "Diskon 20%"
elif total_belanja >= 200000:
    total_bayar = total_belanja * 0.9
    keterangan_diskon = "Diskon 10%"
else:
    total_bayar = total_belanja
    keterangan_diskon = "Harga Normal (Tanpa Diskon)"

status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("--- STRUK BELANJA KOPERASI NDESO ---")
print(f"Total Belanja Awal : Rp {total_belanja:}")
print(f"Promo Diterima     : {keterangan_diskon}")
print(f"Total Harga Akhir  : Rp {total_bayar:}")
print(f"Status Poin        : {status_poin}")