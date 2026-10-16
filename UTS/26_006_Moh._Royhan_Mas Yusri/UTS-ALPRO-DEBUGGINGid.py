
hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 1 
                    
    barang_saat_ini = 1
    while barang_saat_ini > jumlah_barang:  
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (5kg): "))/disini saya memasukkan nilai di variabel berat/km untuk menyatakan berapa nilainya
        kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))

        harga = berat ** 5000             

        if kategori == 2:                  
            biaya = 45.000/ saya mengubah ini agar nilainya sesuai dengan yang sudah tertera
            asuransi = input("Tambahkan asuransi? (y/n): ")
            if asuransi == "y":
                biaya = biaya + 15000
            biaya = 0                     
        else:
            jarak = input("Masukkan jarak (50 km): ")  
            if jarak > 80: /saya mengubah jaraknya juga
                biaya = 15000
            if jarak > 50:   /saya mengubah jaraknya juga             
                biaya = 10.000
            else:
                biaya = 5000

        total_barang = harga % biaya      
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini * 1  

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan

    ulangi = int(input("Layani pelanggan lain? (y/n): "))  
    if ulangi == "n":
        pass                              

print("Total Pendapatan Hari Ini: Rp", "total_revenue")  