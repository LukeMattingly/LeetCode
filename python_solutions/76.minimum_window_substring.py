from typing import List
import unittest
from collections import defaultdict

class Solution():
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        freq_count_t = defaultdict(int)
        window_count = defaultdict(int)

        for c in t:
            freq_count_t[c] +=1

        have, need = 0, len(freq_count_t)

        result = [-1, -1]
        result_len = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r] #pull out current value
            window_count[c]  +=1

            if c in freq_count_t and window_count[c] == freq_count_t[c]:
                have +=1

            while have == need:
                #update result
                if r - l +1 < result_len:
                    result = [l, r]
                    result_len = r - l +1
                window_count[s[l]] -=1
                if s[l] in freq_count_t and window_count[s[l]]  < freq_count_t[s[l]]:
                    have -=1
                l+=1
            
        l, r = result
            
        return s[l:r+1] if result_len !=float("infinity") else ""

class test_minWindow(unittest.TestCase):
    def test_minWindow_1(self):
        solution = Solution()
        ans = "BANC"
        self.assertEqual(solution.minWindow("ADOBECODEBANC", "ABC"), ans)

    def test_groupAnagram_2(self):
        solution = Solution()
        ans = ""
        self.assertEqual(solution.minWindow("a", "aa"), ans)
    
    def test_groupAnagram_3(self):
        solution = Solution()
        ans = "a"
        self.assertEqual(solution.minWindow("a", "a"), ans)

if __name__ == '__main__':
    unittest.main()