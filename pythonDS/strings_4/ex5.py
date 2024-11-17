# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

string1 = input("Enter the string")
string2 = input("Enter the string")

temp1 = string1[0:2]
temp2 = string2[0:2]

string1 = string1.replace(temp1,temp2)
string2 = string2.replace(temp2,temp1)

print(string1)
print(string2)