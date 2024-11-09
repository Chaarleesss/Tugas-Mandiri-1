def rumus_prima(nilai):

    if nilai < 2:
        return False
    
    for i in range(2, int(nilai**0.5) + 1):
        if nilai % i == 0:
            return False
    return True

    
while True :
    number = int(input("Masukkan bilangan : "))

    if number == 0 :
        print("Terimakasih sudah menggunakan penghitungan prima")
        break
    if rumus_prima(number):
        print(f"{number} adalah bilangan Prima.")
    else:
        print(f"{number} bukanlah bilangan Prima.")
            
        
