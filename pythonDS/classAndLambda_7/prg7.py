# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 

class StringReverser:
    @staticmethod
    def reverse_words(s: str) -> str:
        words = s.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

reverser = StringReverser()
input_string = 'hello .py'
output_string = reverser.reverse_words(input_string)
print(output_string)  
