# 1 ~ N 의 합
total = 0
for i in range(1,101):
    total += i
print(total)

# 배열의 총합
arr = [1,4,2,11,1243,2]
total = 0
for i in arr:
    total += i
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

