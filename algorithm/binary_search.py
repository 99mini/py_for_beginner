import random

def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

arr = [random.randint(0,100) for _ in range(100)]
print("====== Init Arr ======")
arr.sort()
print(arr)
target = 4
print(bisect(arr,target))