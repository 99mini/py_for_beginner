# 조건 판단하기
# 과제
# 가위바위보 만들기02
import random

rsp = ['바위', '가위', '보']
while True:
    player = input('바위/가위/보/끝 중에 선택하세요!\n')
    computer = random.choice(rsp)

    # 끝인 경우
    if player == '끝':
        break

    print(player, computer)

    # 비긴 경우
    if player == computer:
        print("Draw...")

    # player 가 이긴 경우
    elif player == '바위' and computer == '가위':
        print("Win...!")
    elif player == '가위' and computer == '보':
        print("Win...!")
    elif player == '보' and computer == '바위':
        print("Win...!")

    # computer 가 이긴 경우
    elif player == '가위' and computer == '바위':
        print("Loss...!")
    elif player == '바위' and computer == '보':
        print("Loss...!")
    elif player == '보' and computer == '가위':
        print("Loss...!")

