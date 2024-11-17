# 20. Write a Python program to remove all consecutive duplicates of a given string.

string = input("Enter the string")
new_string=""

for i in range(0,len(string)-1):
    if string[i]!=string[i+1]:
        new_string+=string[i]

print(new_string)
        
