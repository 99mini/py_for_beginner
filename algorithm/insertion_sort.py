import random

'''
worst case : O(n^2)
best case : O(n)
avg case : O(n^2)
'''

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

arr = [random.randint(0,100000) for _ in range(10000)]
print("====== Init Arr ======")
print(arr)
insertion_sort(arr)
print("\n====== Sorted Arr ======")
print(arr)