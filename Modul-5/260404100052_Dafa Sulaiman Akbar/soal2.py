def cek_palindrom(kata):
    kata = kata.lower()
    terbalik = ""
    for huruf in kata:
        terbalik = huruf + terbalik
    if kata == terbalik:
        return True
    else:
        return False

kata = input("Masukkan kata : ")
hasil = cek_palindrom(kata)
print(hasil)
if hasil:
    print(f"Kata '{kata}' adalah palindrom")
else:
    print(f"Kata '{kata}' bukan palindrom")