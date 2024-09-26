panjang = float(input("Masukan Panjang Ruangan : "))
lebar = float(input("Masukan Lebar Ruangan :  "))
satuan = input("Masukan Satuan (Meter/Inci) : ")


meter1 = panjang*lebar
inci1 = panjang+lebar
satuan1 = satuan.lower()

if satuan1 == "meter" : 
    print("Luas ruangan dengan",panjang ,"dan lebar", lebar, "adalah", meter1)
else :
    print("inci ruangan dengan",panjang ,"dan lebar", lebar, "adalah", inci1)

