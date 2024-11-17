# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 

original_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = "ack"
matching_elements1 = list(filter(lambda s: substring1 in s, original_list))
print(matching_elements1)

substring2 = "abc"
matching_elements2 = list(filter(lambda s: substring2 in s, original_list))
print(matching_elements2)
