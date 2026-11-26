undangan = set()
web_a = set()
web_b = set()

for i in range(int(input("Jumlah undangan: "))):
    undangan.add(input("Nama undangan: "))

for i in range(int(input("Jumlah peserta A: "))):
    web_a.add(input("Nama peserta A: "))

for i in range(int(input("Jumlah peserta B: "))):
    web_b.add(input("Nama peserta B: "))

semua = web_a.union(web_b)
print("\nSemua peserta:", semua)
print("Hadir keduanya:", web_a.intersection(web_b))
print("Hanya salah satu:", web_a.symmetric_difference(web_b))
print("Tidak hadir:", undangan.difference(semua))