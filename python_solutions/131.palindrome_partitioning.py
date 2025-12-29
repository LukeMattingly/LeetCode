from typing import List
import unittest


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(startIndex, partition):
            if startIndex == len(s):
                result.append(partition.copy())
                return
            
            for i in range(startIndex, len(s)):
                subString = s[startIndex:i+1]
                if subString == subString[::-1]:
                    partition.append(subString)
                    backtrack(i+1, partition)
                    partition.pop()
        
        backtrack(0, [])
        return result