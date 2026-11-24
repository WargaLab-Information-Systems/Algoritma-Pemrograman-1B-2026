def cek_palindrom(kata):
    if kata == kata:
        return True
    else:
        return False

teks = input("Masukkan kata : ")

if cek_palindrom(teks):
    print("Kata tersebut adalah Palindrom")
else:
    print("Kata tersebut bukan Palindrom")