'''
0 1 2 3 4 5
1 1 2 3 5 8 13 21 34 ...
'''

def fibo(n):
    if n < 2:
        return 1
    return fibo(n-1) + fibo(n-2)
'''
n=5
fibo(4) + fibo(3)

n=4
fibo(3) + fibo(2)

n=3
fibo(2) + fibo(1)

n=2
fibo(1) + fibo(0)

n=1 
return 1
'''
print(fibo(10))

'''
5! = 1*2*3*4*5 = 120
'''

def fact(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def fact1(n):
    if n == 1:
        return 1
    else:
        return n * fact1(n-1)

'''
n=5
5*fact(4)

n=4
4*fact(3)

n=3
3*fact(2)

n=2
2*fact(1)

n=1
return 1
'''

# print(fact(5))

'''
2진수

1       = 1
10      = 2
100     = 4
1000    = 8
10000   = 16

11      = 3
110     = 6
1100    = 12

1000
0001 0000 
'''