# 11. Write a Python program to sort a dictionary by key.

c={ 3: 30, 4: 40,1: 10, 2: 20}
a=list(c.keys())
a.sort()
b={}
for i in a:
    b[i]=c[i]
print(c)
print(b)