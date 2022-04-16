# using list
# Queue
# FIFO First In First Out 
q = []

# push
q.append(1)
q.append(2)
q.append(3)

print(f'queue: {q}')

# pop
left = q.pop(0)
print(f'left: {left}')
print(f'queue: {q}')

'''
파이썬에서 리스트를 이용할 때 pop 연산 시 O(n)의 복잡도를 같는다.
* pop 후 데이터를 한 칸 씩 옮기는 연산 사용. *
'''

# using queue module
from queue import Queue
que = Queue()

# push
que.put(1)
que.put(2)
que.put(3)
print(f'queue: {que}')

# pop
left = que.get()
print(f'left: {left}')
print(f'queue: {que}')

print(type(que))