
def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    return nilai_akhir, grade, status


nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Nilai tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

nilai, grade, status = hitung_nilai(tugas, uts, uas)

print("=============================")
print("Nama        :", nama)
print("Nilai Akhir :", nilai)
print("Grade       :", grade)
print("Status      :", status)