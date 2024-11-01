def rata_rata_nilai():
    total_nilai = 0
    jumlah_nilai = 0

    while True:
        nilai = input("Masukkan Nilai : ").strip()
        nilai = nilai.upper()
        
        if nilai == '':
            break
        elif nilai == 'A':
            total_nilai += 4.00
            jumlah_nilai += 1
            print("Nilai = 4.00")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'A-':
            total_nilai += 3.75
            jumlah_nilai += 1
            print("Nilai = 3.75")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'B+':
            total_nilai += 3.50
            jumlah_nilai += 1
            print("Nilai = 3.50")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'B':
            total_nilai += 3.00
            jumlah_nilai += 1
            print("Nilai = 3.00")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'B-':
            total_nilai += 2.75
            jumlah_nilai += 1
            print("Nilai = 2.75")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'C+':
            total_nilai += 2.50
            jumlah_nilai += 1
            print("Nilai = 2.50")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'C':
            total_nilai += 2.00
            jumlah_nilai += 1
            print("Nilai = 2.00")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'C-':
            total_nilai += 1.75
            jumlah_nilai += 1
            print("Nilai = 1.75")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'D':
            total_nilai += 1.50
            jumlah_nilai += 1
            print("Nilai = 1.50")
            print(f"Nilai Total : {total_nilai} ")
        elif nilai == 'E':
            total_nilai += 1.25
            jumlah_nilai += 1
            print("Nilai = 1.25")
            print(f"Nilai Total : {total_nilai} ")
        else:
            print(f"Kategori '{nilai}' tidak valid. Silakan coba lagi.")

    if jumlah_nilai == 0:
        print("Tidak ada nilai valid untuk dihitung.")
        return

    rata_rata = total_nilai / jumlah_nilai
    print(f"Rata-rata nilai: {rata_rata:.2f}")

rata_rata_nilai()