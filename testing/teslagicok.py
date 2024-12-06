class Mahasiswa:
    # Constructor untuk menginisialisasi atribut biodata mahasiswa
    def __init__(self, nama, nim, jurusan, umur):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.umur = umur

    # Method untuk menampilkan biodata mahasiswa
    def tampilkan_biodata(self):
        print(f"\nBiodata Mahasiswa:")
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Umur     : {self.umur} tahun")

# Fungsi untuk menginput data mahasiswa
def input_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    jurusan = input("Masukkan jurusan mahasiswa: ")
    umur = int(input("Masukkan umur mahasiswa: "))
    return Mahasiswa(nama, nim, jurusan, umur)

# Program utama
def main():
    mahasiswa_list = []
    total_mahasiswa = 0

    while True:
        print("\nInput data mahasiswa:")
        mhs = input_mahasiswa()
        mahasiswa_list.append(mhs)
        total_mahasiswa += 1
        
        lagi = input("Apakah Anda ingin menambahkan mahasiswa lain? (ya/tidak): ").lower()
        if lagi != "ya":
            break

    # Menampilkan biodata seluruh mahasiswa yang telah diinput
    print("\n\n=== Data Mahasiswa ===")
    for mhs in mahasiswa_list:
        mhs.tampilkan_biodata()

    print(f"\nTotal mahasiswa yang telah diinput: {total_mahasiswa}")

# Memanggil fungsi main untuk menjalankan program
if __name__ == "__main__":
    main()
