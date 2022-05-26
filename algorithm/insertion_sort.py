import random

'''
worst case : O(n^2)
best case : O(n)
avg case : o(n^2)
'''

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

arr = [random.randint(0,1000) for _ in range(100)]
print("====== Init Arr ======")
print(arr)
insertion_sort(arr)
print("\n====== Sorted Arr ======")
print(arr)