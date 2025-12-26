from typing import List
import unittest


class Solution:   
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(visited, permutation):
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    permutation.append(nums[i])
                    backtrack(visited, permutation)
                    permutation.pop()
                    visited[i] = False
        
        backtrack([False]* len(nums), [])
        return result