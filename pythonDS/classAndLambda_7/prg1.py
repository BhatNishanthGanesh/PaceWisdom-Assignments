
# 1) Write a python class to convert an integer into a roman numeral and viceversa

class RomanNumerals:
    int_to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman_to_int_map = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    @classmethod
    def int_to_roman(cls, num):
        res = []
        for value, symbol in cls.int_to_roman_map:
            while num >= value:
                res.append(symbol)
                num -= value
        return ''.join(res)

    @classmethod
    def roman_to_int(cls, roman):
        i = 0
        res = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in cls.roman_to_int_map:
                res += cls.roman_to_int_map[roman[i:i+2]]
                i += 2
            else:
                res += cls.roman_to_int_map[roman[i]]
                i += 1
        return res


print(RomanNumerals.int_to_roman(3457)) 
print(RomanNumerals.roman_to_int('MMMDXLIX'))  
