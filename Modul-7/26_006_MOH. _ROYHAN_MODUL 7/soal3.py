undangan = set()
webinar_a = set()
webinar_b = set()

print("=== INPUT DAFTAR UNDANGAN ===")
jumlah = int(input("Jumlah undangan: "))

for i in range(jumlah):
    nama = input("Nama undangan: ")
    undangan.add(nama)

print("\n=== PESERTA WEBINAR A ===")
jumlah = int(input("Jumlah peserta Webinar A: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_a.add(nama)

print("\n=== PESERTA WEBINAR B ===")
jumlah = int(input("Jumlah peserta Webinar B: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_b.add(nama)

print("\n=== HASIL PENDATAAN ===")

semua_peserta = webinar_a | webinar_b
keduanya = webinar_a & webinar_b
salah_satu = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta

print("Semua peserta:", semua_peserta)
print("Hadir di kedua webinar:", keduanya)
print("Hadir di salah satu webinar:", salah_satu)
print("Undangan yang tidak hadir:", tidak_hadir)