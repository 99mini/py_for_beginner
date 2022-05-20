'''
Worst   : O(n^2)
Avg     : O(n^2 / k), k = # of burket

Space Complex
O(n*k)
'''

arr = [10,41,12,18,21,42,31,79,81,92,22]
burkets = [[]for _ in range(9)]

for number in arr:
    tens = int(number / 10)
    burkets[tens-1].append(number)

for burket in burkets:
    burket.sort()
    for number in burket:
        print(number, end=' ')

