def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)


n = int(input("enter the number of elments"))
arr = [int(input(f"Enter the {i+1} element: ")) for i in range(n)]

quickSort(arr, 0, len(arr)-1) 
print("Sorted array is:", arr) 
