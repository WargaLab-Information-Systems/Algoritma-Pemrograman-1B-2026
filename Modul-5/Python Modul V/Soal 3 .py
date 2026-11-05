
def hitung_nilai(nama, tugas, uts, uas):
    # Menghitung nilai akhir berdasarkan bobot
    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    # Menentukan grade
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    # Menentukan status kelulusan
    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    # Menampilkan hasil
    print("\n===== HASIL NILAI MAHASISWA =====")
    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", nilai_akhir)
    print("Grade          :", grade)
    print("Status         :", status)


# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Memanggil function
hitung_nilai(nama, tugas, uts, uas)
