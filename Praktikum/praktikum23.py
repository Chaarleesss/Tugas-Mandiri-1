class Objek:
    def __init__(self):
        self._nama = ""
        self._nilai = 0

    def get_nama(self):
        return self._nama
    
    def set_nama(self, nama):
        self._nama = nama
    
    def get_nilai(self):
        return self._nilai
    
    def set_nilai(self, nilai):
        self._nilai = nilai

def main():
    objek = Objek()  
    is_objek_tersedia = False  
    
    while True:
        print("\nMenu:")
        print("1. Mendeklarasikan Objek")
        print("2. Menampilkan Objek")
        print("3. Merubah Nilai atau Nama dari Objek")
        print("4. Menghapus Objek")
        print("5. Keluar Program")
        
        try:
            pilihan = int(input("Pilih opsi (1-5): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka antara 1-5.")
            continue
        
        if pilihan == 1:
            nama = input("Masukkan Nama objek: ")
            nilai = int(input("Masukkan Nilai objek: "))
            objek.set_nama(nama)
            objek.set_nilai(nilai)
            print("\nObjek telah berhasil dideklarasikan.")
            is_objek_tersedia = True
        
        elif pilihan == 2:
            if is_objek_tersedia:
                print("\nObjek yang telah dideklarasikan:")
                print(f"Nama: {objek.get_nama()}")
                print(f"Nilai: {objek.get_nilai()}")
            else:
                print("\nObjek belum dideklarasikan. Silakan pilih opsi 1 untuk mendeklarasikan objek.")
        
        elif pilihan == 3:
            if is_objek_tersedia:
                print("\nPilih yang ingin diubah:")
                print("1. Ubah Nama")
                print("2. Ubah Nilai")
                pilihan_ubah = int(input("Pilih opsi (1-2): "))
                
                if pilihan_ubah == 1:
                    nama_baru = input("Masukkan Nama baru: ")
                    objek.set_nama(nama_baru)
                    print("\nNama objek telah diperbarui.")
                elif pilihan_ubah == 2:
                    nilai_baru = int(input("Masukkan Nilai baru: "))
                    objek.set_nilai(nilai_baru)
                    print("\nNilai objek telah diperbarui.")
                else:
                    print("Pilihan tidak valid. Silakan pilih antara 1-2.")
            else:
                print("\nObjek belum dideklarasikan. Silakan pilih opsi 1 untuk mendeklarasikan objek.")
        
        elif pilihan == 4:
            if is_objek_tersedia:
                objek.set_nama("")
                objek.set_nilai(0)
                print("\nObjek telah dihapus.")
                is_objek_tersedia = False
            else:
                print("\nObjek belum dideklarasikan. Tidak ada objek untuk dihapus.")
        
        elif pilihan == 5:
            print("Keluar dari program...")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

if __name__ == "__main__":
    main()
