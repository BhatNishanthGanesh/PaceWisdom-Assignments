# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

n = int(input("Enter n"))
list=[]

for _ in range(n):
    list.append(int(input()))

count = 0

for num in list:
    if num>30:
        count+=1
print(count)