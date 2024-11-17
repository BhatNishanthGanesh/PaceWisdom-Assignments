# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

import math
odd=[]
even=[]
prime=[]

for i in range(1,101):
    flag=0
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
    for j in range(2,(i//2)+1):
        if i%j==0:
            flag=1
            break   
    if flag==0:
        prime.append(i)

print(even)
print(odd)
print(prime)