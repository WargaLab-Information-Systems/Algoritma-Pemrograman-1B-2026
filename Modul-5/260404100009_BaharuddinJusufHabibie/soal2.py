def cek_palindrom(kata):
    if len(kata) <= 1:
        return True
    
    if kata[0] == kata[-1]:
        return cek_palindrom(kata[1:-1])
    else:
        return False

try:
    user_input = input("Masukkan kata: ").strip()
    
    kata_bersih = user_input.lower()
    
    hasil = cek_palindrom(kata_bersih)
    
    if hasil:
        print(f"'{user_input}' adalah palindrom (True).")
    else:
        print(f"'{user_input}' bukan palindrom (False).")
        
except Exception as e:
    print("Terjadi kesalahan:", e)
