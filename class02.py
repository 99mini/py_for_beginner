# 조건문과 랜덤 라이브러리

# 조건문의 기본 구조

score = 100
if score > 90:
    print("참 잘했어요.")
elif score > 70:
    print("잘했어요.")
else:
    print("다음에 더 잘해 보아요.")

# 조건문 논리 연산하기

# and
print(False and False)
print(False and True)
print(True and False)
print(True and True)

# or
print(False or False)
print(False or True)
print(True or False)
print(True or True)

# not
print(not True)
print(not False)

# in
gold_box = ['foo', 'foo', 'gold', 'foo']
if 'gold' in gold_box:
    print("Yes")

import random

# random 0~1
random_number = random.Random()
print(random_number)

# random range [x,y)
for i in range(6):
    random_number = random.randrange(1, 7)
    print(i, "번째: ", random_number)

# 주사위 굴리기 게임
while True:
    if input("주사위를 굴리시겠습니까? Y/N") == 'N':
        break

    random_number = random.randrange(1, 7)
    print(random_number)



