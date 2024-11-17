# 4) Write a Python program to find if a given string starts with a given character using Lambda

string = "hello world"
character = "h"

starts_with = lambda s, c: s.startswith(c)
result = starts_with(string, character)

print(result)
