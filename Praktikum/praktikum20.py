def create_file(nama_file):
    with open(nama_file, 'w') as file:
        print(f"File {nama_file} telah dibuat.")
        data = input("Masukkan data yang ingin ditulis ke file: ")
        file.write(data + '\n')
        print(f"Data '{data}' telah ditulis ke dalam file {nama_file}.")

def read_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            print(f"Isi file {nama_file}: \n")
            print(file.read())
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan!")

def add_file(nama_file):
    with open(nama_file, 'a') as file:
        data = input("Masukkan data yang ingin ditambahkan ke file: ")
        file.write(data + '\n')
        print(f"Data '{data}' telah ditambahkan ke dalam file {nama_file}.")

def show():
    print("\nMenu:")
    print("1. Buat file baru")
    print("2. Baca file")
    print("3. Tambah data ke file")
    print("4. Keluar (Close)")

def main():
    while True:
        show()
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':  
            nama_file = input("Masukkan nama file yang ingin dibuat(contoh : data.txt): ")
            create_file(nama_file)
        
        elif pilihan == '2':  
            nama_file = input("Masukkan nama file yang ingin dibaca: ")
            read_file(nama_file)
        
        elif pilihan == '3':  
            nama_file = input("Masukkan nama file yang ingin ditambahkan data: ")
            add_file(nama_file)
        
        elif pilihan == '4':  
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")


main()
