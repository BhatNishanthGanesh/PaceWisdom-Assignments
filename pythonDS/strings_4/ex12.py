# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

string = input("Enter the string")

upper_count=0

for i in range(0,len(string)):
    i=1
    if string[i]>='A' and string[i]<='Z':
        upper_count+=1
    i+=1
    if i==4:
        break

if upper_count>=2:
    string = string.upper()

print(string)    