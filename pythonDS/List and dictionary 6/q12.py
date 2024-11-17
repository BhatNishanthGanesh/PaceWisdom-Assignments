# 12. Write a Python program to get the maximum and minimum value in a dictionary. 
c={1: 10, 2: 20, 3: 30, 4: 40}
b=list(c.values())
b.sort()
print("minimum",b[0],"maximum",b[len(b)-1])
