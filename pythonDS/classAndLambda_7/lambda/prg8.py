# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 

string = "PaceWisd0m"
is_valid = lambda s: (
    len(s) >= 10 and 
    any(c.islower() for c in s) and 
    any(c.isupper() for c in s) and 
    any(c.isdigit() for c in s)
)
result = is_valid(string)
print("valid string" if result else "invalid string")
