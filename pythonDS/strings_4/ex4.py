# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = input("Enter the string")
char = string[0]
new_string=char

for i in range(1,len(string)):
    if string[i]==char:
        new_string+="$"
    else:
        new_string+=string[i]    

print(new_string)
