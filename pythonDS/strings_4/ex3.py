# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result : Empty String 

string = input("Enter the string")
newString=""
if(len(string)<2):
    print("Empty string")
else:
    newString+=string[0:2]+string[-2:]
    print(newString)
