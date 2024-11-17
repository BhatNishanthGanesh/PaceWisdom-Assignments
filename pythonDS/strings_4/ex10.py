# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

input_sequence = input("Enter the comma seperated words")
words = input_sequence.split(",")
unique_words=set(words)
sorted_letters = sorted(unique_words)

print(sorted_letters)