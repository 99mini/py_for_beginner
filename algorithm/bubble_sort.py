import random
'''
worst case : O(n^2)
best case : O(n)
avg case : o(n^2)
'''
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [random.randint(0,1000) for _ in range(100)]
print("====== Init Arr ======")
print(arr)
bubble_sort(arr)
print("\n====== Sorted Arr ======")
print(arr)
