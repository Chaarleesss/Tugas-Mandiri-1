print("Enter -1 to stop the program")
while True: 
    bulan = input("Enter the month (1-12) : ")
    try:
        bulan = int(bulan)
    except ValueError:
        print("Input not valid, please input it correctly.")
        continue
    if bulan < 1 or bulan > 12:
        print("Data invalid, bye.")
        break
    if bulan == 2:
        tahun = input("Enter the year : ")
        try:
            tahun = int(tahun)
            if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
                print("there 29 days")
            else:
                print("there are 28 days")
        except ValueError:
            print("Input year not valid.")
            continue
    elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
         print("There are 31 days in the month")
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
         print("There are 30 days in the month")
