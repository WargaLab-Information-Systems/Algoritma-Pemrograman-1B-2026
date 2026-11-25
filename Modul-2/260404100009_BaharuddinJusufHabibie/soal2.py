total_belanjaan = int(input("Masukkan total belanjaan Siti (Rp): "))

if total_belanjaan % 100000 == 0:
    diskon = 100
    total_akhir = 0
elif total_belanjaan % 50000 == 0:
    diskon = 50
    total_akhir = total_belanjaan - total_belanjaan * 50 // 100
elif total_belanjaan % 10000 == 0:
    diskon = 20
    total_akhir = total_belanjaan - total_belanjaan * 20 // 100
elif total_belanjaan >= 200000:
    diskon = 10
    total_akhir = total_belanjaan - total_belanjaan * 10 // 100
else:
    diskon = 0
    total_akhir = total_belanjaan

poin = "Poin Bertambah" if total_akhir > 0 else "Tidak Ada Poin"

print(total_belanjaan, "adalah total belanjaan Siti sebelum diskon.")
print("Diskon yang diterapkan: ", diskon, "%")
print("Total belanjaan Siti setelah diskon: Rp", total_akhir)
print("Status Poin: ", poin)

