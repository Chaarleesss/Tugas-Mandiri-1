def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort_recursive(arr, n - 1)

arr = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("List Sebelum di sorting : \n", arr)
sorted_arr = bubble_sort_recursive(arr)
print("List Sesudah di sorting : \n", sorted_arr)
