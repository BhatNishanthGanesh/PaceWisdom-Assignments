# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


a=[{},{},{}]
for i in a:
    if i:
        print("False")
        break
else:
    print("True")