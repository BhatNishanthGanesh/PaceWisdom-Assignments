# 1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
#  Sample Output: 25 48 

add_15 = lambda x: x + 15
multiply = lambda x, y: x * y

number = 10
x = 6
y = 8

result_add = add_15(number)
result_multiply = multiply(x, y)

print(result_add)
print(result_multiply)
