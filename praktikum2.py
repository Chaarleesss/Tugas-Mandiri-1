panjang = int(input("Masukan Panjang Ruangan : "))
lebar = int(input("Masukan Lebar Ruangan :  "))
satuan = input("Masukan Satuan (Meter/Inci) : ")

meter1 = panjang*lebar
inci1 = panjang+lebar

if satuan == "meter" : 
    print("Luas ruangan dengan",panjang ,"dan lebar", lebar, "adalah", meter1)
elif satuan == "Meter" :
        print("Luas ruangan dengan",panjang ,"dan lebar", lebar, "adalah", meter1)
else :
    print("inci ruangan dengan",panjang ,"dan lebar", lebar, "adalah", inci1)

