import random

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [random.randint(0,1000) for _ in range(100)]
print("====== Init Arr ======")
print(arr)
selection_sort(arr)
print("\n====== Sorted Arr ======")
print(arr)

