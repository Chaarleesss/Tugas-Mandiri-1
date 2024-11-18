
def perpangkatan(base, power):
    if power == 0:
        return 1
    elif power > 0:
        return base * perpangkatan(base, power - 1)
    else:
        return 1 / perpangkatan(base, -power)

def main():
    base = float(input("Masukkan angka dasar : "))  
    power = int(input("Masukkan pangkat : ")) 
    
    hasil = perpangkatan(base, power)
    
    print(f"Hasilnya adalah: {hasil}")

main()
