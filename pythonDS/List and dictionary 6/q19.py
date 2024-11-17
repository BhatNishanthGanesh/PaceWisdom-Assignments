# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

a=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)