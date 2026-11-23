def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

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

    print("=== Hasil Perhitungan ===")
    print(f"Nama        : {nama}")
    print(f"Nilai Tugas : {tugas}")
    print(f"Nilai UTS   : {uts}")
    print(f"Nilai UAS   : {uas}")
    print(f"Nilai Akhir : {nilai_akhir}")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")

nama = input("Nama mahasiswa : ")
tugas = float(input("Nilai tugas : "))
uts = float(input("Nilai UTS : "))
uas = float(input("Nilai UAS : "))
print()
hitung_nilai(nama, tugas, uts, uas)