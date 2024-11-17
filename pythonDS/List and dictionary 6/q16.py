# 16. Write a Python program to find the highest 3 values in a dictionary.

d={1: 1, 2: 4, 5: 25, 3: 9, 4: 16}
a=list(d.values())
a.sort(reverse=True)
print(a[0],a[1],a[2])