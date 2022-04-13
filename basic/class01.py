# 00 반복문

# for 문

# 구구단 만들기
n = 9
for i in range(1, n + 1):
    print("{0}단".format(i))
    for j in range(1, n + 1):
        print("{0} X {1} = {2}".format(i, j, i * j))

# 특정 구구단만 출력하기
target = int(input("몇 단을 출력할까요? "))

for i in range(1, n + 1):
    # 만약에 타겟 단이면 실행한다.
    if i == target:
        print("{0}단".format(i))
        for j in range(1, n + 1):
            print("{0} X {1} = {2}".format(i, j, i * j))
    else:
        pass

people = ['진수', '상민', '후석', '예선', '은지']
ages = [12, 20, 31, 24, 15]

# for 문 range 활용
for i in range(5):
    print("{0}의 나이는 {1}이다.".format(people[i], ages[i]))

# for 문 if 문 활용
# 예선의 나이만 출력
for i in range(5):
    if people[i] == '예선':
        print("{0}의 나이는 {1}이다.".format(people[i], ages[i]))

# for 문 iterable (이터러블: 반복 가능한 객체)
for person in people:
    print(person)

# for 문 zip 활용
# zip 평행한 반복자 (Parallel Iteration)
for person, age in zip(people, ages):
    print("{0}의 나이는 {1}이다.".format(person, age))

print("=" * 20)

# for 문 enumerate 활용
for index, person in enumerate(people):
    print("{0}은 {1}번이다.".format(person, index))
