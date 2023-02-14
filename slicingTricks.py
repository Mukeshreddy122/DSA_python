a=[1,2,3,4,5,5]

# 1) Trick 1: reversing the list 
print(a[::-1])

# 2) Trick 2 : copying all the elements into another list 
b=a[:]
print(b)

# 3) Trick 3: If we need elements in odd indexes
print(a[::2])

# 4) Trick 4: First three elements in the list 
print(a[0:3])

# 5) Trick 5: Last three elements in the list 
print(a[-3:])

