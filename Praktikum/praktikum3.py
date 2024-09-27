import math

a = float(input("Masukan Nilai A = "))
b = float(input("Masukan Nilai B = "))

penjumlahan = a + b
selisih = a-b
perkalian = a * b
sisabagi = a % b
bagi = a / b
pangkat = a**b
logaritma = math.log10(a)


print(f"Hasil dari penjumlahan A+B adalah = {penjumlahan}")
print(f"Selisih antara A dan B adalah = {selisih}")
print(f"Jumlah A dikali B adalah = {perkalian}")
print(f"Jumlah sisa pembagian dari Hasil A dibagi B adalah = {sisabagi}")
print(f"Jumlah A dibagi B adalah = {bagi}")
print(f"Hasil dari log(A) adalah = {logaritma}")
print(f"HasiL A pangkat B adalah = {pangkat}")