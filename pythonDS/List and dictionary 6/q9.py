# 9. Write a Python program to multiply all the items in a dictionary.

c={1: 10, 2: 20, 3: 30, 4: 40}
sum=1
for i in c:
    sum*=c[i]
print(sum)