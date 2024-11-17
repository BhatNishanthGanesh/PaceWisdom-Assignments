# 15. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
a=[]
b={}
for i in d1:
    a.append(i)
for j in d2:
    if j not in a:
        a.append(j)
for i in a:
    if i in d1 and i in d2:
        b[i]=d1[i]+d2[i]
    elif i in d1:
        b[i]=d1[i]
    else:
        b[i]=d2[i]
print(b)

print(Counter(d1)+Counter(d2))