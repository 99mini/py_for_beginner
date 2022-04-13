# 딕셔너리 dict
# key : 변하지 않는 값
# value :
#       변하거나 변하지 않는 값 모두 가능
#       value에는 어떤 자료형도 올 수 있음
# 리스트나 튜플처럼 순차적으로 값을 얻지 않음

hamburger_stores = {
    '롯데리아': '새우버거',
    '맘스터치': '싸이버거',
    '맥도날드': '빅맥',
    '버거킹': '와퍼',
}

# 값에 접근하기
print(hamburger_stores['롯데리아'])
hamburger_stores['롯데리아'] = '불고기버거'
print(hamburger_stores.get('롯데리아'))

# 키와 값
keys = hamburger_stores.keys()
values = hamburger_stores.values()

print("key의 값은 ", keys)
print("value의 값은 ", values)
for key, value in zip(keys, values):
    print("{0}의 대표 메뉴는 {1}이다.".format(key, value))