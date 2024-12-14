class Data:
    def __init__(self):
        self._nama = ""
        self._umur = 0
    
    # Getter dan Setter untuk nama
    def get_nama(self):
        return self._nama
    
    def set_nama(self, nama):
        self._nama = nama
    
    # Getter dan Setter untuk umur
    def get_umur(self):
        return self._umur
    
    def set_umur(self, umur):
        self._umur = umur


def main():
    data = Data()  # Membuat objek Data
    is_data_tersedia = False
    
    while True:
        # Menampilkan menu
        print("\nMenu:")
        print("1. Menambahkan & Menampilkan Objek")
        print("2. Mengubah & Menampilkan Objek")
        print("3. Menghapus & Menampilkan Objek")
        print("4. Keluar")
        
        try:
            pilihan = int(input("Pilih opsi (1-4): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka antara 1-4.")
            continue

        if pilihan == 1:
            # Menambahkan & Menampilkan Objek
            nama_baru = input("Masukkan Nama: ")
            umur_baru = int(input("Masukkan Umur: "))
            data.set_nama(nama_baru)
            data.set_umur(umur_baru)
            print("\nData yang ditambahkan:")
            print(f"Nama: {data.get_nama()}")
            print(f"Umur: {data.get_umur()}")
            is_data_tersedia = True
        
        elif pilihan == 2:
            # Mengubah & Menampilkan Objek
            if is_data_tersedia:
                nama_ubah = input("Masukkan Nama baru: ")
                umur_ubah = int(input("Masukkan Umur baru: "))
                data.set_nama(nama_ubah)
                data.set_umur(umur_ubah)
                print("\nData setelah perubahan:")
                print(f"Nama: {data.get_nama()}")
                print(f"Umur: {data.get_umur()}")
            else:
                print("Data belum ada. Silakan tambahkan data terlebih dahulu.")
        
        elif pilihan == 3:
            # Menghapus & Menampilkan Objek
            if is_data_tersedia:
                data.set_nama("")
                data.set_umur(0)
                print("\nData telah dihapus.")
                is_data_tersedia = False
            else:
                print("Data belum ada untuk dihapus.")
        
        elif pilihan == 4:
            # Keluar
            print("Keluar dari program...")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")


if __name__ == "__main__":
    main()
