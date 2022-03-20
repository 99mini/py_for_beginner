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