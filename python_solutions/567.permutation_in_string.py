from typing import List
import unittest
from collections import defaultdict

class Solution():
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_count_s1 = defaultdict(int)
        freq_count_window = defaultdict(int)

        for s in s1:
            freq_count_s1[s] += 1

        left = 0
        for right in range(len(s2)):
            freq_count_window[s2[right]] += 1

            #if window size exceeds s1 remove leftmost character
            if right - left +1 > len(s1):
                freq_count_window[s2[left]] -=1
                if freq_count_window[s2[left]] ==0:
                    del freq_count_window[s2[left]]
                left+=1
            
            if freq_count_window == freq_count_s1:
                return True

        return False


class test_checkInclusion(unittest.TestCase):
    def test_checkInclusion_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.checkInclusion("ab", "eidbaooo"), ans)

    def test_checkInclusion_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.checkInclusion("ab", "eidboaoo"), ans)
    


if __name__ == '__main__':
    unittest.main()