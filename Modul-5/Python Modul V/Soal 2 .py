def cek_palindrom(kata):
    kata = kata.lower()
    return kata == kata[::-1]

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

print("Kata pertama palindrom:", cek_palindrom(kata1))
print("Kata kedua palindrom:", cek_palindrom(kata2))