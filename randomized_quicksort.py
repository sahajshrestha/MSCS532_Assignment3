import random

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        p = partition(arr, low, high)
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
