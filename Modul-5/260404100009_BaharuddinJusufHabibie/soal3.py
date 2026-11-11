def hitung_nilai_mahasiswa(nama, tugas, uts, uas):
    # Hitung nilai akhir dengan bobot: Tugas 30%, UTS 30%, UAS 40%
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade in ["A", "B", "C"]:
        status = "Lulus"
    else:
        status = "Tidak Lulus"
        
    print("\nHASIL PENILAIAN AKHIR MAHASISWA")
    print("="*40)
    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS :", uts)
    print("Nilai UAS :", uas)
    print("Nilai Akhir : {:.2f}".format(nilai_akhir))
    print("Grade :", grade)
    print("Status :", status)

try:
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    hitung_nilai_mahasiswa(nama, tugas, uts, uas)
except ValueError:
    print("Input nilai tidak valid! Harap masukkan angka untuk nilai tugas, UTS, dan UAS.")
