# 과제
# 반복문과 조건문을 이용하여 달력 출력하기
# 출력 예시
# 1월은 31일까지 있습니다.
# 2월은 28일까지 있습니다.
# 3월은 30이까지 있습니다
i = 1
thirty_one = [1, 3, 5, 7, 8, 10, 12]
thirty = [4, 6, 9, 11]
for i in range(1,13):
    print("{0} 월은".format(i), end=' ')
    # 31일 까지 있는 경우
    if i in thirty_one:
        print("{0} 일까지 있습니다.".format(31))
    # 30일까지 있는 경우
    elif i in thirty:
        print("{0} 일까지 있습니다.".format(30))
    # 28일까지 있는 경우
    else:
        print("{0} 일까지 있습니다.".format(28))