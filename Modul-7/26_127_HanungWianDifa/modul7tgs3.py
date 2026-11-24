
# PROGRAM PENGELOLAAN PESERTA WEBINAR

undangan = set()
webinar_a = set()
webinar_b = set()

print(" INPUT DATA UNDANGAN ")
jumlah = int(input("Jumlah undangan: "))

for i in range(jumlah):
    nama = input("Nama undangan: ")
    undangan.add(nama)

print("\n PESERTA WEBINAR A ")
jumlah = int(input("Jumlah peserta Webinar A: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_a.add(nama)

print("\n PESERTA WEBINAR B ")
jumlah = int(input("Jumlah peserta Webinar B: "))

for i in range(jumlah):
    nama = input("Nama peserta: ")
    webinar_b.add(nama)

# Operasi himpunan
semua_peserta = webinar_a | webinar_b
peserta_keduanya = webinar_a & webinar_b
peserta_satu_webinar = webinar_a ^ webinar_b
tidak_hadir = undangan - semua_peserta

print("\n HASIL DATA WEBINAR ")

print("\nSemua peserta kedua webinar:")
print(semua_peserta)

print("\nPeserta yang hadir di kedua webinar:")
print(peserta_keduanya)

print("\nPeserta yang hanya hadir di salah satu webinar:")
print(peserta_satu_webinar)

print("\nUndangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)
