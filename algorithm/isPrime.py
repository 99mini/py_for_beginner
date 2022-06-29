# 에라토스테네스의 체
# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
n = 9999999

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

# 단순 소수 판별
# O(n)
def isPrime(number):
  for i in range(2,number-1):
    if number % i == 0:
      return False
  return True

print(prime_list(n))
# primes1= []
# for i in range(2,n+1):
#   if isPrime(i):
#     primes1.append(i)

# print(primes1)
# number = int(input())

# if isPrime(number):
#   print("is prime")
# else:
#   print("is not prime")

'''
144

1 * 144
2 * 72
3 * 48
4 * 
...
12 * 12   # sqrt(n)
...
48 * 3
72 * 2

'''