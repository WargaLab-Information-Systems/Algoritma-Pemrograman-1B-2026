def palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]


kata = input("Masukkan satu kata: ")

hasil = palindrom(kata)
if hasil:
    print(f"'{kata}' adalah PALINDROM.")
else:
    print(f"'{kata}' BUKAN palindrom.")