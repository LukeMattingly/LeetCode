from typing import List
import unittest
from collections import defaultdict

class Solution():
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        count_array = [[] for _ in range(len(nums)+1)]
        result = []

        for num in nums:
            freq_map[num] +=1
        
        for n, count in freq_map.items():
            count_array[count].append(n)
        
        count = 0
        for numbers in reversed(count_array):
           if numbers:
                for value in numbers:
                    if count < k:
                        result.append(value)
                        count +=1
                    else:
                        return result

        return result



class test_canConstruct(unittest.TestCase):
    def test_canConstruct_1(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.topKFrequent([1,1,1,2,2,3], 2 ), ans)

    def test_canConstruct_2(self):
        solution = Solution()
        ans = [1]
        self.assertEqual(solution.topKFrequent([1],1), ans)
    
    def test_canConstruct_3(self):
        solution = Solution()
        ans = [4,2]
        self.assertEqual(solution.topKFrequent([1, 2, 2, 3, 4, 4, 4], 2), ans)


if __name__ == '__main__':
    unittest.main()