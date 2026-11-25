undangan = set()
webinar_A = set()
webinar_B = set()

print("DATA UNDANGAN")
while True:
    nama = input("Nama undangan (selesai untuk berhenti): ")
    if nama == "selesai":
        break
    undangan.add(nama)

print("PESERTA WEBINAR A")
while True:
    nama = input("Nama peserta (selesai untuk berhenti): ")
    if nama == "selesai":
        break
    webinar_A.add(nama)

print("PESERTA WEBINAR B")
while True:
    nama = input("Nama peserta (selesai untuk berhenti): ")
    if nama == "selesai":
        break
    webinar_B.add(nama)

semua = webinar_A | webinar_B
keduanya = webinar_A & webinar_B
satu = webinar_A ^ webinar_B
tidak_hadir = undangan - semua

print("HASIL DATA WEBINAR")
print("Semua peserta:", semua)
print("Mengikuti kedua webinar:", keduanya)
print("Hanya mengikuti satu webinar:", satu)
print("Tidak mengikuti webinar:", tidak_hadir)