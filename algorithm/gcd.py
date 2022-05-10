# 196 38 gcd
# 유클리드 호제법

'''
Q       r1      r2      r
5       196     38      6
6       38      6       2
3       6       2       0
        2       0

최대 공약수 = 2
'''

# using recursive
def gcd1(r1,r2):
    if(r2==0):
        return r1
    else:
        return gcd1(r2,r1%r2)

# using while
def gcd2(r1,r2):
    while(r2):
       r1, r2 = r2, r1 % r2
  
    return r1
