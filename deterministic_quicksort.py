def deterministic_quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        deterministic_quicksort(arr, low, p - 1)
        deterministic_quicksort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1
