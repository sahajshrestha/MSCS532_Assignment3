import random
import time
from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort

def benchmark(sort_func, arr):
    copied = arr.copy()
    start = time.perf_counter()
    sort_func(copied, 0, len(copied) - 1)
    return time.perf_counter() - start

def generate_inputs(n):
    return {
        "Random": random.sample(range(n * 10), n),
        "Sorted": list(range(n)),
        "Reversed": list(range(n, 0, -1)),
        "Duplicates": [random.choice(range(10)) for _ in range(n)],
    }

if __name__ == "__main__":
    input_sizes = [1000, 5000, 10000]
    for size in input_sizes:
        print(f"\nInput size: {size}")
        inputs = generate_inputs(size)
        for desc, arr in inputs.items():
            time_rand = benchmark(randomized_quicksort, arr)
            time_determ = benchmark(deterministic_quicksort, arr)
            print(f"{desc}: Randomized: {time_rand:.5f}s, Deterministic: {time_determ:.5f}s")
