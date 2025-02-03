from typing import List
import unittest

class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0 
        unique_chars = set()

        for right in range(len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left +=1
            
            unique_chars.add(s[right])
            max_length = max(max_length, right- left +1)

        return max_length
    
class test_lengthOfLongestSubstring(unittest.TestCase):
    def test_lengthOfLongestSubstring_1(self):
        solution = Solution()
        ans = 3
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), ans)

    def test_lengthOfLongestSubstring_2(self):
        solution = Solution()
        ans = 1
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), ans)
    
    def test_lengthOfLongestSubstring_3(self):
        solution = Solution()
        ans = 3
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), ans)
    
    def test_lengthOfLongestSubstring_3(self):
        solution = Solution()
        ans = 3
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), ans)
    

if __name__ == '__main__':
    unittest.main()