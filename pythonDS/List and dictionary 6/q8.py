# 8.  Write a Python program to sum all the items in a dictionary.

c={1: 10, 2: 20, 3: 30, 4: 40}
a=list(c.values())
print(sum(a))

#or in another way

sum=0
for i in c:
    sum+=c[i]
print(sum)