# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

# Examples
# The following are examples of balanced delimiter strings:

# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

# Input:
# ([{}])
# Output:
# True

delimeter=input("Enter the string: ")
stack=[]
flag=1

for char in delimeter:
    if char=='{' or char=='(' or char=='[':
        stack.append(char)
    elif (char==')' and stack[-1]=='(')or(char=='}' and stack[-1]=='{')or(char==']' and stack[-1]=='['):
        stack.pop()
    else:
        break

if not stack:
    print("True")
else:
    print("False")