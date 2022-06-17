import random


def linearSearch(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    

arr = [random.randint(0,100) for _ in range(100)]
print("====== Init Arr ======")
print(arr)
target = 4
print(linearSearch(arr,target))