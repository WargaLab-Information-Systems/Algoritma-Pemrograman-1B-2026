undangan = set(input("Nama undangan : ").split())
A = set(input("Peserta Webinar A: ").split())
B = set(input("Peserta Webinar B: ").split())

print("Semua peserta:", A | B)
print("Hadir di kedua webinar:", A & B)
print("Hanya Webinar A:", A - B)
print("Hanya Webinar B:", B - A)
print("Tidak hadir:", undangan - (A | B))