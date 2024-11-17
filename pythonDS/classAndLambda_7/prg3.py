# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 

class Subsets:
    @classmethod
    def find_subsets(cls, nums):
        result = []
        subset = []

        def backtrack(start):
            result.append(subset[:])  
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        
        backtrack(0)
        return result


nums = [4, 5, 6]
print(Subsets.find_subsets(nums))
