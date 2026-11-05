hitung = True
total_pendapatan = 0
kategori=0
jumlah_barang=0
berat=0
#variabel diatas tidak ditulis dengan lengkap

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 1  
    berat = int(input("Masukkan berat paket (kg): "))
    kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))
    jarak = input("Masukkan jarak (km): ")  
    barang_saat_ini = 1
    print("Barang", barang_saat_ini)
    while barang_saat_ini > jumlah_barang:  
        harga = berat ** 5000             
#program kode diatas salah penempatan
        if kategori == 2:                  
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (y/n): ")
            if asuransi == "y":
                biaya = biaya + 15000
            biaya = 0                     
    if jarak > 100:
        biaya = 15000
    if jarak > 20:                
        biaya = 10000
    #kode ini salah penempatan harusnya bearada di kondisi while pertama.
                    
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

print("Total Pendapatan Hari Ini: Rp", total_pendapatan) #salah penulisan variabel.