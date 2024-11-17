
# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 

class ArrayPairFinder:
    @classmethod
    def find_pair(cls, numbers, target):
        index_map = {}
        for index, num in enumerate(numbers):
            complement = target - num
            if complement in index_map:
                return (index_map[complement]+1, index+1)
            index_map[num] = index
        return None

numbers = [90, 20, 10, 40, 50, 60, 70]
target = 50
result = ArrayPairFinder.find_pair(numbers, target)
if result:
    print(result)
else:
    print("No pair found")
