def jumlah_func(angka_list, index=0):
    if index == len(angka_list):
        return 0
    else:
        return angka_list[index] + jumlah_func(angka_list, index + 1)

def main():
    jumlah = int(input("Masukkan Jumlah: "))  
    angka_list = []

    for i in range(1, jumlah + 1):
        angka = int(input(f"Masukkan angka ke-{i}: "))
        angka_list.append(angka)
    
    hasil = jumlah_func(angka_list)
    
    print(f"Hasil penjumlahan: {hasil}")

main()
