# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


a=int(input("Enter the n:"))
b={}
for i in range(1,a+1):
    b[i]=i**2
print(b)