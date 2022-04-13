rsp = ['바위', '가위', '보']
player = rsp[0]
computer = rsp[1]

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
