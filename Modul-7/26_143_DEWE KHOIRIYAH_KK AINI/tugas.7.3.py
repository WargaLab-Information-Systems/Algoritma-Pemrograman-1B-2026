# Membuat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()

# Mengisi daftar undangan
print("=== INPUT DAFTAR UNDANGAN ===")
jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input(f"Nama undangan ke-{i+1}: ")
    undangan.add(nama)

# Mengisi peserta Webinar A
print("\n=== INPUT PESERTA WEBINAR A ===")
jumlah = int(input("Masukkan jumlah peserta Webinar A: "))

for i in range(jumlah):
    nama = input(f"Nama peserta ke-{i+1}: ")
    webinar_A.add(nama)

# Mengisi peserta Webinar B
print("\n=== INPUT PESERTA WEBINAR B ===")
jumlah = int(input("Masukkan jumlah peserta Webinar B: "))

for i in range(jumlah):
    nama = input(f"Nama peserta ke-{i+1}: ")
    webinar_B.add(nama)

# Operasi himpunan
semua_peserta = webinar_A | webinar_B
peserta_keduanya = webinar_A & webinar_B
hanya_satu = webinar_A ^ webinar_B
tidak_hadir = undangan - (webinar_A | webinar_B)

# Menampilkan hasil
print("\n===== HASIL DATA WEBINAR =====")

print("Semua peserta dari kedua webinar:")
print(semua_peserta)

print("\nPeserta yang hadir di kedua webinar:")
print(peserta_keduanya)

print("\nPeserta yang hanya hadir di salah satu webinar:")
print(hanya_satu)

print("\nUndangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)