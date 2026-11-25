def cek_palindrom(kata):
    kata = ''.join(kata.lower().split())

    if kata == kata[::-1]:
        return True
    else:
        return False

teks = input("Masukkan kata atau kalimat: ")

if cek_palindrom(teks):
    print("Kata tersebut adalah Palindrom")
else:
    print("Kata tersebut bukan Palindrom")