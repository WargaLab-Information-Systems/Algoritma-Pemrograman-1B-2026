# kode = int(input("masukkan kode rahasia 3 digit:"))

# if kode < 100 or kode > 999:
#     print("kode harus 3 digit (100-999)!")
# else:
#     #nilai digit
#     d1 = kode // 100
#     d2 = (kode // 10) % 10
#     d3 = kode % 10
#     print("digit pertama :", d1)
#     print("digit kedua   :", d2)
#     print("digit ketiga  :", d3)

#     #nilai pelacak awal
#     pelacak = d1 * d3
#     print("nilai pelacak awal:", pelacak)

#     #perubahan tahap 1
#     if d2 % 2 == 1:
#         pelacak = pelacak + 25
#     else:
#         pelacak = pelacak - d2
#     print("nilai pelacak setelah tahap 1:", pelacak)

#     #perubahan tahap 2
#     if pelacak % 3 == 0:
#         pelacak = pelacak // 3
#     else:
#         pelacak = pelacak * 2
#     print("nilai pelacak setelah tahap 2:", pelacak)

#     #status password
#     if pelacak > 50:
#         print("status: password kategori A")
#     elif pelacak > 20:
#         print("status: password kategori B")
#     else:
#         print("status: password ditolak")


#Program Perintah if
nama = "malik"
if nama == "malik":
    print ("hallo " + nama)


kunci = "python"
password = input("masukkan password : ")
if password == kunci :
    print("password benar")
else:
    print("password salah")


#Program Perintah if-elif-else
angka = int(input("masukkan sebuah bilangan : "))
if angka > 0:
    print("angka merupakan bilangan positif")
elif:angka < 0:
    print("angka merupan bilangan negatif")
else:
    print("angka merupakan 0")


#Program if bersarang
x = int(input("masukkan nilai x="))
y = int(input("masukkan nilay y="))
if x == y:
    print("nilai", x ,"dan",y ,"mempunyai niali yang sama")
else:
    if x > y :
        print(x, "lebih besar daripada", y)
    else:
        print(x, "lebih kecil daripada", y)

: a = 10
b = 20
#contoh mengembalikan nilai pada ternary 
opet = "opet harus belajar" if a < b else "opet tak perlu belajar" print(opet) 

#angka ke kata
a = int(input("masukkan angka (0-9): "))
if a == 0:
    print("angka anda nol")
elif a == 1:
    print("angka anda satu")
elif a == 2:
    print("angka anda dua")
elif a == 3:
    print("angka anda tiga")
elif a == 4:
    print("angka anda empat")
elif a == 5:
    print("angka anda lima")
elif a == 6:
    print("angka anda enam")
elif a == 7:
    print("angka anda tujuh")
elif a == 8:
    print("angka anda delapan")
elif a == 9:
    print("angka anda sembilan")
else:
    print("angka anda not found")