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

for i in range(3):
    for j in range(3-i):
        print(' ',end='')
    stars = i*2+1
    print('*'*stars)
