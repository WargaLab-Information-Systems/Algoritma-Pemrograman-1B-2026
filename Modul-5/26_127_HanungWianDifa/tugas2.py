
def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

# Input kata dari pengguna
kata = input("Masukkan sebuah kata: ").lower()

# Memanggil fungsi
hasil = palindrom(kata)

# Menampilkan hasil
if hasil == True:
    print(kata, "merupakan kata palindrom")
else:
    print(kata, "bukan merupakan kata palindrom")

    