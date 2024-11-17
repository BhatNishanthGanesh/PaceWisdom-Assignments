# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

string = input("Enter the string")

frequency_map = {}

for char in string:
    if char not in frequency_map:
        frequency_map[char]=1
    else:
        frequency_map[char]+=1;    

for char,frequency in frequency_map.items():
    if frequency!=1:
        print(char," ",frequency)