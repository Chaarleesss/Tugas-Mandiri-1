nama = input("Masukan Nama anda : " )
nilai_Tugas = float(input("Masukan Nilai Tugas Anda : "))
nilai_UTS = float(input("Masukan Nilai UTS Anda : "))
nilai_UAS = float(input("Masukan Nilai UAS Anda : "))

niilai_Akhir = (0.3 * nilai_Tugas + 0.3 * nilai_UTS + 0.4 * nilai_UAS)

if(niilai_Akhir >  100.0) :
    print("nilai anda tidak valid")
else :
    print(f"Nilai Akhir {nama} adalah : {niilai_Akhir:.2f}")


#punya pak anung
# nama = input("Masukan Nama anda : " )
# nilai_Tugas = float(input("Masukan Nilai Tugas Anda : "))
# while nilai_Tugas < 0.0 or nilai_Tugas > 100.0:
#     nilai_Tugas = float(input("Masukan Nilai Tugas Anda : "))

# nilai_UTS = float(input("Masukan Nilai UTS Anda : "))
# nilai_UAS = float(input("Masukan Nilai UAS Anda : "))

# niilai_Akhir = 0.3 * nilai_Tugas + 0.3 * nilai_UTS + 0.4 * nilai_UAS

# if(niilai_Akhir >  100.0) :
#     print("nilai anda tidak valid")
# else :
#     print(f"Nilai Akhir {nama} adalah : {niilai_Akhir:.2f}")

# x = 1
# y = 2
# coba = (x**3)/3 - (x*y**2) + (y**2)
# print(coba)