# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

n = int(input("Enter the value of n"))
sum=0
for i in range(0,n):
    sum+=int(input())
    
print("Sum is", sum)
print("Avergae is",sum//n)    