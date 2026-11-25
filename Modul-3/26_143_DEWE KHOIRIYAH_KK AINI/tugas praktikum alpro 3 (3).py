jumlah_mahasiswa = 10
total_nilai = 0
nilai_tertinggi = -1
nilai_terendah  = 101
nama_tertinggi=""
nama_terendah=""
kat_a=kat_b=kat_c=kat_d=kat_e = 0
for i in range(1,jumlah_mahasiswa+1):
    nama = input ("nama : ")
    tugas = float(input("nilai tugas(30%):"))
    uts = float(input("nilai uts(30%):"))
    uas = float(input("nilai uas(40%):"))
    nilai_akhir = (0.3*tugas)+(0.3*uts)+(0.4*uas)
    total_nilai += nilai_akhir
    if nilai_akhir>=85 :
        kat ='a'
        kat_a+=1
    elif nilai_akhir>=75:
        kat='b'
        kat_b+=1
    elif nilai_akhir>=65:
        kat ='c'
        kat_c+=1
    elif nilai_akhir>= 50:
        kat='d'
        kat_d+=1
    else :
        kat ='e'
        kat_e+=1
    print("nilai akhir:",nilai_akhir)
    if nilai_akhir > nilai_tertinggi :
        nilai_tertinggi=nilai_akhir
        nama_tertinggi =nama
    if nilai_akhir<nilai_terendah:
        nilai_terendah =nilai_akhir
        nama_terendah =nama
    print ("jumlah kategori A:",kat_a)
    print ("jumlah kategori B:",kat_b)
    print ("jumlah kategori C:",kat_c)
    print ("jumlah kategori D:",kat_d)
    print ("jumlah kategori E:",kat_e)
    print ("nilai tertinggi :",nilai_tertinggi)
    print ("nama tertinggi :",nama_tertinggi)
    print ("nilai terendah:",nilai_terendah)
    print ("nama terendah:",nama_terendah)
    print ("rata rata kelas:",total_nilai)
