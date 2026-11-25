total = 0
jumlah = 0

nilai = int(input("Masukkan nilai tugas (-99 untuk selesai): "))

while nilai != -99:
    total = total + nilai
    jumlah = jumlah + 1
    nilai = int(input("Masukkan nilai tugas (-99 untuk selesai): "))

print("Total nilai seluruh tugas:", total)
print("Banyaknya tugas yang diinputkan:", jumlah)