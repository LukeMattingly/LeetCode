from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(subset, index):
            if len(nums)== index:
                result.append(subset.copy())
                return 
            
            subset.append(nums[index])
            backtrack(subset, index+1)

            subset.pop()
            backtrack(subset, index+1)
        
        backtrack([], 0)
        return result