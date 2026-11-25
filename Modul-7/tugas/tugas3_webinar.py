undangan = set()
webinar_a = set()
webinar_b = set()

print("=== Input Daftar Undangan (ketik 'selesai' untuk berhenti) ===")
while True:
    nama = input("Nama undangan: ")
    if nama == "selesai":
        break
    undangan.add(nama)

print("\n=== Input Peserta Webinar A (ketik 'selesai' untuk berhenti) ===")
while True:
    nama = input("Nama peserta A: ")
    if nama == "selesai":
        break
    webinar_a.add(nama)

print("\n=== Input Peserta Webinar B (ketik 'selesai' untuk berhenti) ===")
while True:
    nama = input("Nama peserta B: ")
    if nama == "selesai":
        break
    webinar_b.add(nama)

semua = webinar_a | webinar_b       
keduanya = webinar_a & webinar_b
salah_satu = webinar_a ^ webinar_b
tidak_hadir = undangan - semua

print("\n=== HASIL ===")
print("Semua peserta kedua webinar      :", semua)
print("Peserta yang hadir di keduanya   :", keduanya)
print("Peserta hanya di salah satu      :", salah_satu)
print("Undangan tidak hadir di mana pun :", tidak_hadir)
