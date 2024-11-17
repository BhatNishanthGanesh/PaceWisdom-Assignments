# 9. Write a Python program to remove the nth index character from a nonempty string.

string = input("Enter the string")
n = int(input("Enter the index value"))

string = string.replace(string[n],"",1)
print(string)

