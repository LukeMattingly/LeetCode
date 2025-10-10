from typing import List
import unittest

class Solution():
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for val in nums:
            currSum+=val
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0

        return maxSum           
            



if __name__ == '__main__':
    unittest.main()