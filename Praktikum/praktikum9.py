# 'A' == 4.00
# 'A-' == 3.75
# 'B+' == 3.50
# 'B' == 3.00
# 'B-' == 2.75
# 'C+' == 2.50
# 'C' == 2.00
# 'C-' == 1.75
# 'D' == 1.50
# 'E' == 1.25

value_num = 0
jumlah_rata = 0

while True :

    nilai = input("Masukan Nilai : ")
    nilai = nilai.upper()

    if(nilai == '') :
        print("bentar ya di itung dulu")
        break
    elif(nilai == 'A' ) :
        value_num += 4.00
        jumlah_rata += 1
        print(f"Nilai = 4.00")
    elif(nilai == 'A-' ) :
        value_num += 3.75
        jumlah_rata += 1
        print(f"Nilai = 3.75")
    elif(nilai == 'B+' ) :
        value_num += 3.50
        jumlah_rata += 1
        print(f"Nilai = 3.50")
    elif(nilai == 'B' ) :
        value_num += 3.00
        jumlah_rata += 1
        print(f"Nilai = 3.00")
    elif(nilai == 'B-' ) :
        value_num += 2.75
        jumlah_rata += 1
        print(f"Nilai = 2.75")
    elif(nilai == 'C+' ) :
        value_num += 2.50
        jumlah_rata += 1
        print(f"Nilai = 2.50")
    elif(nilai == 'C' ) :
        value_num += 2.00
        jumlah_rata += 1
        print(f"Nilai = 2.00")
    elif(nilai == 'C-' ) :
        value_num += 1.75
        jumlah_rata += 1
        print(f"Nilai = 1.75")
    elif(nilai == 'D' ) :
        value_num += 1.50
        jumlah_rata += 1
        print(f"Nilai = 1.50")
    elif(nilai == 'E' ) :
        value_num += 1.25
        jumlah_rata += 1
        print(f"Nilai = 1.25")
    else :
        print("Nilai yang anda masukan tidak valid,Masukan lagi")
    
if value_num == 0 :
    print("Tidak ada nilai yang dapat dihitung")
    
rata_rata = value_num / jumlah_rata
print(f"rata-rata nilai : {rata_rata}")


