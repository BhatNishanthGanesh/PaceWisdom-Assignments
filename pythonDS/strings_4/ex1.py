# 1. Write a Python program to calculate the length of a string.

string = input("Enter the string")
length = 0

for char in string:
    length+=1

print("Length of the string: ",length)    