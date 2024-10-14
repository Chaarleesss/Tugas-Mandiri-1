nama = input("Masukan Nama anda : " )
nilai_Tugas = int(input("Masukan Nilai Tugas Anda : "))
nilai_UTS = int(input("Masukan Nilai UTS Anda : "))
nilai_UAS = int(input("Masukan Nilai UAS Anda : "))

niilai_Akhir = (0.3 * nilai_Tugas + 0.3 * nilai_UTS + 0.4 * nilai_UAS)

if(niilai_Akhir >  100) :
    print("nilai anda tidak valid")
else :
    print(f"Nilai Akhir {nama} adalah : {niilai_Akhir}")