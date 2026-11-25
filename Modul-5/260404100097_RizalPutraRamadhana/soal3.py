def hitung_nilai(nama, tugas, uts, uas): 
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4) 
 
    if nilai_akhir >= 85: 
        grade = "A" 
    elif nilai_akhir >= 70: 
        grade = "B" 
    elif nilai_akhir >= 55: 
        grade = "C" 
    else: 
        grade = "D" 
 
    if grade == "A" or grade == "B" or grade == "C":
                status = "Lulus" 
    else: 
        status = "Tidak Lulus" 
 
    print("\n=== HASIL NILAI MAHASISWA ===") 
    print("Nama Mahasiswa :", nama) 
    print("Nilai Tugas    :", tugas) 
    print("Nilai UTS      :", uts) 
    print("Nilai UAS      :", uas) 
    print("Nilai akhir    :", f"{nilai_akhir:.2f}") 
    print("Grade          :", grade) 
    print("Status         :", status) 
 
nama = input("Masukkan nama mahasiswa: ") 
 
while True: 
    tugas = float(input("Nilai tugas : ")) 
    if 0 <= tugas <= 100: 
        break 
    print("Nilai harus 0-100! Input ulang.") 
 
while True: 
    uts = float(input("Nilai UTS   : ")) 
    if 0 <= uts <= 100: 
        break 
    print("Nilai harus 0-100! Input ulang.") 
 
while True: 
    uas = float(input("Nilai UAS   : ")) 
    if 0 <= uas <= 100: 
        break 
    print("Nilai harus 0-100! Input ulang.") 
 
hitung_nilai(nama, tugas, uts, uas)