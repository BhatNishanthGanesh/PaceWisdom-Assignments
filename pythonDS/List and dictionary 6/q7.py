# 7. Write a Python script to merge two Python dictionaries.

a={1:10, 2:20}
b={3:30, 4:40}
c={}
for i in a:
    c[i]=a[i]
for j in b:
    c[j]=b[j]
print(c)