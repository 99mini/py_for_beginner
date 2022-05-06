# find max / min

list1 = [1,3,2,9,10,20,1010,24]

max_number = -1


for i in range(len(list1)):
    if list1[i] > max_number:
        max_number = list1[i]

print("max number = ", max_number)

