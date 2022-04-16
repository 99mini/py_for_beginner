# stack
# FILO First In Last Out
s = []

# push
s.append(1)
s.append(2)
s.append(3)
print(f'stack: {s}')

# pop
top = s.pop()
print(f'top: {top}')
print(f'stack: {s}')

# # top
top = s[-1]
print(f'top: {top}')
print(f'stack: {s}')

# size
print(f"size: {len(s)}")