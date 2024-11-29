def main() : 
    arr = [2, 15, 23, 28, 31, 34, 200, 100, 1]
    arr.sort()

    print(arr)
    

    while True:
        try :
            target = int(input("Target : "))
            
            index = arr.index(target)
            print(f'Elemen {target} ditemukan pada indeks', index)
            break

        except ValueError:
            print(f"Elemen {target} tidak ditemukan dalam list setelah sorting")
            break
    

main()

