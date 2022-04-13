# 별 찍기1
# *
# **
# ***
# ****
# *****

for i in range(6):
    for j in range(i):
        print('*', end='')
    print()
print()

# 별 찍기 2
#    *
#   ***
#  *****

level = int(input())
for i in range(level):
    for j in range(level-i-1):
        print(' ',end='')
    stars = i*2+1
    print('*'*stars)

# 별 찍기 3
#      *
#     * *
#    * * *
#   * * * *

for i in range(level):
    print(' ' * (level-i-1), end='')
    for j in range(1,2*i+1):
        if j % 2 ==0:
            print(' ',end='')
        else:
            print('*',end='')
    print()