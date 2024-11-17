# 10. Write a Python program to remove a key from a dictionary. 


c={1: 10, 2: 20, 3: 30, 4: 40}
a=int(input("Enter the key to remove:"))
for i in c:
    if a==i:
        c.pop(i)
        print(c)
        break
else:
    print("No such items")