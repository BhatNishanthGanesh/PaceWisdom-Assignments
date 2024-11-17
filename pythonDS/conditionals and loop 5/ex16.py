# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

list=[]
n = int(input("Enter n"))
for _ in range(n):
    list.append(int(input()))

key = int(input("Enter the key to remove"))
print(list)

for num in list:
    if num==key:
        list.remove(num)

print(list)        