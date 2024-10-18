value_num = 0
jumlah_rata = 0

while True :

    nilai = input("Masukan Nilai : ")
    nilai = nilai.upper()

    if(nilai == '') :
        break
    elif(nilai == 'A' ) :
        value_num += 4.00
        jumlah_rata += 1
        print("Nilai = 4.00")
    elif(nilai == 'A-' ) :
        value_num += 3.75
        jumlah_rata += 1
        print("Nilai = 3.75")
    elif(nilai == 'B+' ) :
        value_num += 3.50
        jumlah_rata += 1
        print("Nilai = 3.50")
    elif(nilai == 'B' ) :
        value_num += 3.00
        jumlah_rata += 1
        print("Nilai = 3.00")
    elif(nilai == 'B-' ) :
        value_num += 2.75
        jumlah_rata += 1
        print("Nilai = 2.75")
    elif(nilai == 'C+' ) :
        value_num += 2.50
        jumlah_rata += 1
        print("Nilai = 2.50")
    elif(nilai == 'C' ) :
        value_num += 2.00
        jumlah_rata += 1
        print("Nilai = 2.00")
    elif(nilai == 'C-' ) :
        value_num += 1.75
        jumlah_rata += 1
        print("Nilai = 1.75")
    elif(nilai == 'D' ) :
        value_num += 1.50
        jumlah_rata += 1
        print("Nilai = 1.50")
    elif(nilai == 'E' ) :
        value_num += 1.25
        jumlah_rata += 1
        print("Nilai = 1.25")
    else :
        print(f"Kategori huruf {nilai} tidak valid dan akan diabaikan")
    
if value_num == 0 :
    print("Tidak ada nilai yang dapat dihitung")
    
rata_rata = value_num / jumlah_rata
print(f"rata-ratanya adalah : {rata_rata}")


