print("Ketik 0 Untuk Menghentikan Program")
def ordinal_number(angka):
    if 10 <= angka % 100 <= 20:
        ordinal = 'th'  
    else:
        if angka % 10 == 1:
            ordinal = 'st'
        elif angka % 10 == 2:
            ordinal = 'nd'
        elif angka % 10 == 3:
            ordinal = 'rd'
        else:
            ordinal = 'th'
        
    return f"({angka} , '{ordinal}')"

def main():
    while True:
        try:
            user_input = int(input("Masukkan angka: "))
            print(ordinal_number(user_input))
            
            if user_input == 0 :
                print("Terimakasih telah menggunakan program saya")
                break

        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")

main()
