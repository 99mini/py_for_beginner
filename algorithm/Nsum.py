# 1 ~ N 의 합
total = 0
for i in range(1,101):
    total += i
print(total)

# 배열의 총합
arr = [1,4,2,11,1243,2]
total = 0

for i in range(6):
    total += arr[i]

for i in range(len(arr)):
    if i == 4:
        print("4번째는", arr[i])
    if arr[i] == 11:
        print("11을 찾았습니다.", i,"번째에 있습니다.")
    total += arr[i]

for (index, something) in enumerate(arr):
    if index == 4:
        print(something)
    if something == 11:
        print("11을 찾았습니다.", index,"번째에 있습니다.")
print(total)

sum_of_arr = sum(arr)
print(sum_of_arr)
# 배열의 요소의 개수

count = 0
for i in arr:
    count+=1
print(count)

len_of_arr = len(arr)
print(len_of_arr)

# 배열의 평균 값
print(total/count)