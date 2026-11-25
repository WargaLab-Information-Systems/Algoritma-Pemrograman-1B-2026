def palindrom(kata): 
    if kata == kata[::-1]: 
        return True 
    else: 
        return False 
 
kata = input("Masukkan sebuah kata: ").lower() 
hasil = palindrom(kata) 
 
if hasil == True: 
    print("Kata", kata, "merupakan palindrom.") 
else: 
    print("Kata", kata, "bukan palindrom.")