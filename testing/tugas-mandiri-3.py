def baca_data(file_input):
    peserta = []
    try:
        with open(file_input, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    nama, nilai = line.rsplit(",", 1)
                    peserta.append((nama.strip(), float(nilai.strip())))
    except FileNotFoundError:
        print(f"File {file_input} tidak ditemukan.")
        return []
    return peserta

def hitung_statistik(peserta):
    total_peserta = len(peserta)
    if total_peserta == 0:
        return total_peserta, 0, None, None, []

    total_nilai = sum(nilai for _, nilai in peserta)
    rata_rata = total_nilai / total_peserta

    lulus = [nama for nama, nilai in peserta if nilai > 80]
    lulus_tertinggi = max((peserta[i] for i in range(len(peserta)) if peserta[i][1] > 80), key=lambda x: x[1], default=None)
    lulus_terendah = min((peserta[i] for i in range(len(peserta)) if peserta[i][1] > 80), key=lambda x: x[1], default=None)

    return total_peserta, rata_rata, lulus_tertinggi, lulus_terendah, lulus

def tulis_hasil(file_output, total_peserta, rata_rata, lulus_tertinggi, lulus_terendah, lulus):
    with open(file_output, 'w') as file:
        file.write(f"Total jumlah peserta: {total_peserta}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")

        if lulus_tertinggi:
            file.write(f"Peserta dengan nilai tertinggi: {lulus_tertinggi[0]} ({lulus_tertinggi[1]:.2f})\n")
        if lulus_terendah:
            file.write(f"Peserta dengan nilai terendah: {lulus_terendah[0]} ({lulus_terendah[1]:.2f})\n")

        file.write("=== Daftar peserta LULUS UJI sertifikasi ===\n")
        for nama in lulus:
            for peserta in peserta_data:
                if peserta[0] == nama:
                    file.write(f"{peserta[0]} ({peserta[1]:.2f})\n")

def main():
    file_input = input("Ketik nama file data: ")
    file_output = input("Ketik nama file hasil: ")

    peserta_data = baca_data(file_input)

    if peserta_data:
        total_peserta, rata_rata, lulus_tertinggi, lulus_terendah, lulus = hitung_statistik(peserta_data)
        tulis_hasil(file_output, total_peserta, rata_rata, lulus_tertinggi, lulus_terendah, lulus)
        print(f"Hasil telah disimpan dalam {file_output}")
    else:
        print("Tidak ada data peserta yang dapat diproses.")


if __name__ == "__main__":
    main()