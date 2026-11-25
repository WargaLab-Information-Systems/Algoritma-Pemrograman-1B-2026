def polindrom(kata):
    return kata == kata[::-1]

kata = input("Masukkan kata: ")
if polindrom(kata):
    print(kata, "adalah polindrom, karena kalo dibalik tetap menjadi", kata[::-1])
else:
    print(kata, "bukan polindrom, karena kalo dibalik menjadi", kata[::-1])