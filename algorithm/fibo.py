'''
0 1 2 3 
1 1 2 3 5 8 13 21 34 ...
'''

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

print(fact(5))

