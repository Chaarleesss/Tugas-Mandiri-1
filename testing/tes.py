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

# def f(x) :
#    return  x**3 + 2*x
# def g(x, y, z) :
#    return x*z + y**2

# a = f(5) + g(1, 8, 4)
# print(a)


# def ucapan(nama) : 
#     print(f"halo, {nama}")

# nama = input("Masukan Nama : ")
# ucapan(nama)

# def kali(a, b) :
#     return a * b

# print(f"hasil perkalian = {kali(2, 2)}")

# import math

# def hitung_sisi_miring(a, b):
#     c = math.sqrt(a**2 + b**2)
#     return c

# a = int(input("Masukan panjang sisi pertama : "))
# b = int(input("Masukan panjang sisi Kedua : "))


# print(f"Panjang sisi miring adalah: {hitung_sisi_miring(a, b)}")

# def faktorial(n) :
#     if n == 1 :
#         return 1
#     else :
#         x = n*faktorial(n-1)
#         return x
    
# def fibonaci(n) :
#     if n==1 or n==2 :
#         return 1
#     else :
#         return fibonaci(n-1)+fibonaci(n-2)
     
# n = int(input("Masukan angka gc : "))
# # print(faktorial(n))
# print(fibonaci(n))


def baca_data(file_name):
    peserta = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                # Memisahkan nama dan nilai
                parts = line.strip().split(",")
                if len(parts) == 2:
                    nama = parts[0].strip()
                    try:
                        nilai = float(parts[1].strip())
                        peserta.append((nama, nilai))
                    except ValueError:
                        print(f"Data nilai tidak valid untuk peserta {nama}")
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return peserta

def hitung_rekap(peserta):
    total_peserta = len(peserta)
    if total_peserta == 0:
        return 0, 0, None, None, []
    
    total_nilai = sum(nilai for _, nilai in peserta)
    rata_rata = total_nilai / total_peserta
    
    peserta_lulus = [nama for nama, nilai in peserta if nilai > 80]
    
    peserta_lulus_tertinggi = max(peserta, key=lambda x: x[1] if x[1] > 80 else -1, default=None)
    peserta_lulus_terendah = min(peserta, key=lambda x: x[1] if x[1] > 80 else float('inf'), default=None)
    
    return total_peserta, rata_rata, peserta_lulus_tertinggi, peserta_lulus_terendah, peserta_lulus

def tulis_rekap_hasil(file_name, total_peserta, rata_rata, peserta_tertinggi, peserta_terendah, peserta_lulus):
    with open(file_name, "w") as file:
        file.write(f"Total jumlah peserta: {total_peserta}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        
        if peserta_tertinggi:
            file.write(f"Peserta dengan nilai tertinggi: {peserta_tertinggi[0]} ({peserta_tertinggi[1]:.2f})\n")
        
        if peserta_terendah:
            file.write(f"Peserta dengan nilai terendah: {peserta_terendah[0]} ({peserta_terendah[1]:.2f})\n")
        
        file.write("\n=== Daftar peserta LULUS UJI sertifikasi ===\n")
        for nama in peserta_lulus:
            file.write(f"{nama}\n")

def main():
    # Minta nama file input dan output
    nama_file_data = input("Ketik nama file data: ")
    nama_file_hasil = input("Ketik nama file hasil: ")
    
    # Membaca data dari file
    peserta = baca_data(nama_file_data)
    
    if peserta:
        # Menghitung rekap
        total_peserta, rata_rata, peserta_tertinggi, peserta_terendah, peserta_lulus = hitung_rekap(peserta)
        
        # Menulis hasil ke file
        tulis_rekap_hasil(nama_file_hasil, total_peserta, rata_rata, peserta_tertinggi, peserta_terendah, peserta_lulus)
        print(f"Rekap hasil sertifikasi telah ditulis ke {nama_file_hasil}")
    else:
        print("Tidak ada data peserta yang valid.")

if __name__ == "__main__":
    main()










