# jam_mulai = int(input("Masukkan jam mulai: "))
# menit_mulai = int(input("Masukkan menit mulai: "))
# jam_selesai = int(input("Masukkan jam selesai: "))
# menit_selesai = int(input("Masukkan menit selesai: "))

# total_menit_mulai = jam_mulai * 60 + menit_mulai
# total_menit_selesai = jam_selesai * 60 + menit_selesai
    
# selisih_menit = total_menit_selesai - total_menit_mulai
    
# if selisih_menit < 0:
#     selisih_menit += 24 * 60 

# jam_selisih = selisih_menit // 60
# menit_selisih = selisih_menit % 60

        
# print(f"Selisih waktu adalah: {jam_selisih} jam dan {menit_selisih} menit")

# while True:
#     try:
#         jam_mulai = int(input("Masukkan jam mulai: "))
#         menit_mulai = int(input("Masukkan menit mulai: "))
#         jam_selesai = int(input("Masukkan jam selesai: "))
#         menit_selesai = int(input("Masukkan menit selesai: "))

#         total_menit_mulai = jam_mulai * 60 + menit_mulai
#         total_menit_selesai = jam_selesai * 60 + menit_selesai
    
#         selisih_menit = total_menit_selesai - total_menit_mulai
    
#         if selisih_menit < 0:
#             selisih_menit += 24 * 60 

#         jam_selisih = selisih_menit // 60
#         menit_selisih = selisih_menit % 60

        
#         print(f"Selisih waktu di antara kedua waktu tersebut adalah {jam_selisih} jam dan {menit_selisih} menit")
#         lagi = input("Apakah anda mau melakukan perhitungan yang lain (Y/T) ? ").strip().lower()
#         if lagi != 'ya':
#             print("Terima kasih telah menggunakan program saya (Programmer)")
#             break
#     except ValueError:
#         print("Input tidak valid, silakan masukkan angka yang benar.")

# def rata_rata_nilai():
#     # Kamus untuk konversi nilai huruf ke angka
#     total_nilai = 0
#     jumlah_nilai = 0

#     while True:
#         huruf = input("Masukkan kategori huruf (atau 'selesai' untuk menghitung rata-rata): ").strip()
        
#         if huruf == 'selesai':
#             break
#         elif huruf == 'A':
#             total_nilai += 4.00
#             jumlah_nilai += 1
#         elif huruf == 'A-':
#             total_nilai += 3.75
#             jumlah_nilai += 1
#         elif huruf == 'B+':
#             total_nilai += 3.50
#             jumlah_nilai += 1
#         elif huruf == 'B':
#             total_nilai += 3.00
#             jumlah_nilai += 1
#         elif huruf == 'B-':
#             total_nilai += 2.75
#             jumlah_nilai += 1
#         elif huruf == 'C+':
#             total_nilai += 2.50
#             jumlah_nilai += 1
#         elif huruf == 'C':
#             total_nilai += 2.00
#             jumlah_nilai += 1
#         elif huruf == 'C-':
#             total_nilai += 1.75
#             jumlah_nilai += 1
#         elif huruf == 'D':
#             total_nilai += 1.50
#             jumlah_nilai += 1
#         elif huruf == 'E':
#             total_nilai += 1.25
#             jumlah_nilai += 1
#         else:
#             print(f"Kategori '{huruf}' tidak valid. Silakan coba lagi.")

#     # Menghitung rata-rata
#     if jumlah_nilai == 0:
#         print("Tidak ada nilai valid untuk dihitung.")
#         return

#     rata_rata = total_nilai / jumlah_nilai
#     print(f"Rata-rata nilai: {rata_rata:.2f}")

# # Contoh penggunaan
# rata_rata_nilai()

def f(x) :
   return  x**3 + 2*x
def g(x, y, z) :
   return x*z + y**2

a = f(5) + g(1, 8, 4)
print(a)


