total_bayar = 0

print("=== Selamat Datang Di Kebun Binatang Trisakti ===")
while True:
    try:
        umur = int(input("Masukkan umur : "))

        if umur <= 2:
            harga_tiket = 0
            print("Gratis")
            print(f"Running Total : ${total_bayar:.2f} ")
        elif 3 <= umur <= 12:
            harga_tiket = 14
            total_bayar += harga_tiket
            print("Harga : $14")
            print(f"Running Total : ${total_bayar:.2f} ")
        elif umur >= 65:
            harga_tiket = 18
            total_bayar += harga_tiket
            print("Harga : $18")
            print(f"Running Total : ${total_bayar:.2f} ")
        else:
            harga_tiket = 23
            total_bayar += harga_tiket
            print("Harga : $23")
            print(f"Running Total : ${total_bayar:.2f} ")

    except ValueError:
       break

print(f"\nTotal harga tiket keseluruhan: ${total_bayar:.2f}")

try:
    pembayaran = float(input("Masukkan jumlah uang yang dibayarkan: $"))

    if pembayaran >= total_bayar:
        kembalian = pembayaran - total_bayar
        print(f"Running Kembalian: ${kembalian:.2f}")
        print("=== Terimakasih ===")
    else:
        kekurangan = total_bayar - pembayaran
        print(f"Uang tidak cukup. Anda masih kekurangan: ${kekurangan:.2f}")
except ValueError:
    print("Input tidak valid. Silakan masukkan jumlah uang yang benar.")