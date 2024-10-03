def hitung_selisih_waktu(jam_mulai, menit_mulai, jam_selesai, menit_selesai):
    # Menghitung total menit dari waktu mulai dan selesai
    total_menit_mulai = jam_mulai * 60 + menit_mulai
    total_menit_selesai = jam_selesai * 60 + menit_selesai

    # Menghitung selisih waktu
    selisih_menit = total_menit_selesai - total_menit_mulai

    # Jika selisih negatif, artinya waktu selesai di hari berikutnya
    if selisih_menit < 0:
        selisih_menit += 24 * 60  # Menambahkan 24 jam dalam menit

    # Menghitung jam dan menit dari selisih menit
    jam_selisih = selisih_menit // 60
    menit_selisih = selisih_menit % 60

    return jam_selisih, menit_selisih

while True:
    try:
        # Input waktu mulai
        jam_mulai = int(input("Masukkan jam mulai: "))
        menit_mulai = int(input("Masukkan menit mulai: "))

        # Input waktu selesai
        jam_selesai = int(input("Masukkan jam selesai: "))
        menit_selesai = int(input("Masukkan menit selesai: "))

        # Hitung selisih waktu
        jam_selisih, menit_selisih = hitung_selisih_waktu(jam_mulai, menit_mulai, jam_selesai, menit_selesai)

        # Tampilkan hasil
        print(f"Selisih waktu adalah: {jam_selisih} jam dan {menit_selisih} menit")

        # Tanya pengguna apakah ingin menghitung lagi
        lagi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").strip().lower()
        if lagi != 'ya':
            break
    except ValueError:
        print("Input tidak valid, silakan masukkan angka yang benar.")
