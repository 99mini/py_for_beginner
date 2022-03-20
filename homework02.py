# random 0~1
import random

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