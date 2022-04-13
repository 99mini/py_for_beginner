# in
gold_box = ['foo', 'foo', 'gold', 'foo']
if 'gold' in gold_box:
    print("Yes")

# 튜플 tuple
# 변화하지 않는 리스트
# immutable 이뮤터블
names = ('박건우', '김영민')
# names[0] = '김건우'
# 튜플의 요소를 변화시킬 수 없음

if '박건우' in names:
    print("Yes")

print(names[0])
# print(*names, sep='\n')
for name in names:
    print(name)

names = '박건우', '김영민'
print(names)

학생, 선생님 = names

print(학생, 선생님)