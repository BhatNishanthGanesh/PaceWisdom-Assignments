# 11. Write a Python function to reverses a string if it's length is a multiple of 4. 

string = input("Enter the string")
reversed_string=""
if(len(string)%4==0):
    for i in range(len(string)-1, -1 ,-1):
        reversed_string+=string[i]
    
print(reversed_string)   