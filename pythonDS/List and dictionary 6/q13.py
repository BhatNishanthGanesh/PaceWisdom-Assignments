# 13. Write a Python program to remove duplicates from Dictionary.

c={1: 10, 2: 20, 3: 30, 4: 40,5:40}
a=[]
b=[]
for i in c:
    if c[i] not in a:
        a.append(c[i])
    else:
        b.append(i)
for i in b:
    c.pop(i)
print(c)