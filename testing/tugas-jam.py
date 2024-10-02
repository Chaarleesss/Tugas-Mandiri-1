def hitung_selisih_waktu(jam_mulai, menit_mulai, jam_selesai, menit_selesai):
    # Menghitung total menit untuk waktu mulai dan selesai
    total_menit_mulai = jam_mulai * 60 + menit_mulai
    total_menit_selesai = jam_selesai * 60 + menit_selesai
    
    # Menghitung selisih waktu dalam menit
    selisih_menit = total_menit_selesai - total_menit_mulai
    
    # Jika selisih negatif, berarti waktu selesai di hari berikutnya
    if selisih_menit < 0:
        selisih_menit += 24 * 60  # Tambahkan 24 jam dalam menit
    
    # Menghitung jam dan menit dari selisih menit
    jam_selisih = selisih_menit // 60
    menit_selisih = selisih_menit % 60
    
    return jam_selisih, menit_selisih

# Input dari pengguna
jam_mulai = int(input("Masukkan jam mulai: "))
menit_mulai = int(input("Masukkan menit mulai: "))
jam_selesai = int(input("Masukkan jam selesai: "))
menit_selesai = int(input("Masukkan menit selesai: "))

# Menghitung selisih waktu
jam_selisih, menit_selisih = hitung_selisih_waktu(jam_mulai, menit_mulai, jam_selesai, menit_selesai)

# Menampilkan hasil
print(f"Selisih waktu: {jam_selisih} jam dan {menit_selisih} menit")