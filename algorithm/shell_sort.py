import random
'''
best    : O(n)
worst   : O(n^2)
avg     : O(n^1.5)
'''

def shell_sort(arr):
    N = len(arr)
    h = N // 2
    while h > 0:
        for i in range(h,N):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j+h] = arr[j]
                j -= h
            arr[j+h] = temp
        h //= 2

arr = [random.randint(0,1000) for _ in range(100)]
print("====== Init Arr ======")
print(arr)
shell_sort(arr)
print("\n====== Sorted Arr ======")
print(arr)
