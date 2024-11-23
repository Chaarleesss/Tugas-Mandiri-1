def perpangkatan(base, pangkat):
    if pangkat == 0:
        return 1
    elif pangkat > 0:
        return base * perpangkatan(base, pangkat - 1)
    else:
        return 1 / perpangkatan(base, -pangkat)

def main():
    base = float(input("Masukkan angka dasar : "))  
    pangkat = int(input("Masukkan pangkat : ")) 
    
    hasil = perpangkatan(base, pangkat)
    
    print(f"Hasilnya adalah: {hasil}")

main()
