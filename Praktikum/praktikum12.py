def count_tahun(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

def jumlah_hari(bulan, tahun):
    if bulan == 2:
        if count_tahun(tahun):
            return 29 
        else:
            return 28  
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return "Bulan tidak ada / valid"  

def main():
    print("Masukan Angka 0 untuk mengentikan program")
    while True:
        try:
            bulan = int(input("Masukkan bulan (1-12): "))
            if bulan == 0 :
                print("terimakasih karna sudah menggunakan program kami")
                break
            tahun = int(input("Masukkan tahun: "))
            if bulan < 1 or bulan > 12:
                print("Bulan tidak valid! Harap masukkan bulan antara 1 sampai 12.")
                continue  
            else:
                hari = jumlah_hari(bulan, tahun)
                print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari} hari.")
                continue  
        except ValueError:
            # Menangani input yang bukan angka
            print("Input tidak valid. Harap masukkan angka untuk bulan dan tahun.")
        
            

main()
