def tulis_biodata():
    nama = input("Masukan Nama mu: ")
    umur = input("Masukan Umur mu: ")
    alamat = input(" Masukan Alamatmu: ")
    email = input("Masukan Emailmu: ")
    dosen_wali = input("Masukan Dosen Wali: ")

    with open("../data/Biodata.txt", "w") as file:
        file.write(f"Nama: {nama}\n")
        file.write(f"Umur: {umur}\n")
        file.write(f"Alamat: {alamat}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Dosen Wali: {dosen_wali}\n")

def baca_biodata():
    try:
        with open("../data/Biodata.txt", "r") as file:
            print("\nBerikut ini data kamu:")
            print(file.read())
    except FileNotFoundError:
        print("File Biodata.txt tidak ditemukan.")

tulis_biodata()
baca_biodata()
