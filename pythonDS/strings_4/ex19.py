# 19. Write a Python program to find smallest and largest word in a given string.

string = input("Enter the string")

new_list = string.split(" ")

print(new_list)

len_max_word = 0
len_min_word = 1000000

for word in new_list:

   if len(word)>len_max_word:
      len_max_word = len(word)
      max_word = word
      
   if len(word)<len_min_word:
      len_min_word =len(word)
      min_word = word
    

print("Max word",max_word)
print("Min word",min_word)        
