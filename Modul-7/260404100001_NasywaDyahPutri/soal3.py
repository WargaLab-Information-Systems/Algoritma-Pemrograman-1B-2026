#buat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()

#ngisi daftar undangan
print("== INPUT DAFTAR UNDANGAN ==")
data = input("Masukkan nama undangan (pisahkan dengan koma): ")
undangan = set(data.split(","))

#ngisi peserta Webinar A
print("\n== INPUT PESERTA WEBINAR A ==")
data = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_A = set(data.split(","))

#ngisi peserta Webinar B
print("\n== INPUT PESERTA WEBINAR B ==")
data = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_B = set(data.split(","))

#hapus spasi di awal dan akhir nama
undangan = {nama.strip() for nama in undangan}
webinar_A = {nama.strip() for nama in webinar_A}
webinar_B = {nama.strip() for nama in webinar_B}

# 1. Semua peserta dari kedua webinar
semua_peserta = webinar_A | webinar_B

# 2. Peserta yang hadir di kedua webinar
peserta_keduanya = webinar_A & webinar_B

# 3. Peserta yang hanya hadir di salah satu webinar
peserta_satu = webinar_A ^ webinar_B

# 4. Undangan yang tidak hadir di webinar mana pun
tidak_hadir = undangan - semua_peserta

# Menampilkan hasil
print("\n== HASIL DATA WEBINAR ==")

print("\nSemua peserta kedua webinar:")
print(semua_peserta)

print("\nPeserta yang hadir di kedua webinar:")
print(peserta_keduanya)

print("\nPeserta yang hanya hadir di salah satu webinar:")
print(peserta_satu)

print("\nUndangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)
