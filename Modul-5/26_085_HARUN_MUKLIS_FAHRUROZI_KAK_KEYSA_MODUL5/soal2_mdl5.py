def palindrom(kata):
    balik = kata[::-1]

    if kata == balik:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ")

hasil = palindrom(kata)

if hasil == True:
    print("Kata", kata, "merupakan palindrom")
else:
    print("Kata", kata, "bukan palindrom")
