# function 함수

def plus(a,b):
    return a+b

def plus_n_minus(b,a):
    return a+b, a-b

result = plus_n_minus(a=-10,b=5)

# 리턴 값이 없는 경우
def gugudan(dan):
    for i in range(1,dan+1):
        print(f'{i}단...')
        for j in range(1,10):
            print(f'{i} X {j} = {i*j}')

gugudan(3)

# 리턴 값이 있는 경우
def power(밑, 지수):
    return 밑 ** 지수

print(power(2,10))

# 함수 이름이 있는 파라미터
print(power(밑=2, 지수=10))

# 리턴 값이 여러개인 경우
def func_devision(피제수, 제수):
    return 피제수 // 제수, 피제수 % 제수

몫, 나머지 = func_devision(11,3)
print(f'11 나누기 3의 몫은 {몫}이고 나머지는 {나머지}이다')


