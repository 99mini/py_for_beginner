# 튜플 tuple
# 변화하지 않는 리스트
names = ('박건우', '김영민', '이상민', '원예선')
# names[0] = '김건우'
# 튜플의 요소를 변화시킬 수 없음

# print(*names, sep='\n')
for name in names:
    print(name)

print('#' * 50)
# 딕셔너리 dict
# key : 변하지 않는 값
# value :
#       변하거나 변하지 않는 값 모두 가능
#       value에는 어떤 자료형도 올 수 있음
# 리스트나 튜플처럼 순차적으로 값을 얻지 않음

people_info = {
    '진수': 12,
    '상민': 20,
    '후석': 31,
    '예선': 24,
    '은지': 15,
}

keys = people_info.keys()
values = people_info.values()

print("key의 값은 ", keys)
print("value의 값은 ", values)
for key, value in zip(keys, values):
    print("{0}의 나이는 {1}이다.".format(key, value))
