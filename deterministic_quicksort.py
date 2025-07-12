def deterministic_quicksort(arr, low, high):
    while low < high:
        p = partition(arr, low, high)
        # Tail call optimization to avoid deep recursion
        if p - low < high - p:
            deterministic_quicksort(arr, low, p - 1)
            low = p + 1
        else:
            deterministic_quicksort(arr, p + 1, high)
            high = p - 1

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1
