print("=== PROGRAM PEMERIKSAAN LAMPU TAMAN PAK DIMAS ===")
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

# Perulangan luar untuk baris
for baris in range(1, jumlah_baris + 1):
  print(f"\n--- Memeriksa Baris ke-{baris} ---")

  # Perulangan dalam untuk lampu di setiap baris
  for lampu in range(1, jumlah_lampu + 1):
    if lampu % 3 == 0:
      print(f"Lampu ke-{lampu}: Mengalami gangguan")
    else:
      print(f"Lampu ke-{lampu}: Berfungsi normal")

# Pesan akhir setelah seluruh lampu diperiksa
print("\n[INFO] Seluruh lampu pada baris terakhir telah selesai diperiksa.")
print("[PERHATIAN] Silakan periksa sumber listrik utama taman!")