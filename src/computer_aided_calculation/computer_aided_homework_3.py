b = ['ab' for _ in range(6)]

for i in range(9):
    b.append(2);

for i in range(14):
    b.append('z')

print(b)

# 1
b[-1] = 'last'
print(b)

# 2
b[len(b)//2] = 'x'
print(b)

# 3
b[1:2] = 'a', 2, 'zz'
print(b)

# 4
del(b[3:10])
print(b)

# 5
b.remove(2)
print(b)

# 6
b[2:12] = b[11:1:-1]

# index of first occurrence of 2
first_occur = b.index(2)
print(first_occur)

# count of occurrences of 2 in b
occurs_count = b.count(2)
print(occurs_count)
