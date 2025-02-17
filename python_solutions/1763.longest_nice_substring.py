from typing import List
import unittest


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        window_size = len(s)
        
        while window_size:
            for i in range(len(s) - window_size + 1):
                substring = s[i:i + window_size] #window + i 
                
                if len(set(substring.lower())) == (len(set(substring)) // 2): #how to determine if it's 'nice'
                    return substring
                
            window_size -= 1
            
        return ''
    
    
class test_longestNiceSubstring(unittest.TestCase):
    def test_longestNiceSubstring_1(self):
        solution = Solution()
        ans = "aAa"
        self.assertEqual(solution.longestNiceSubstring("YazaAay"), ans)

    def test_longestNiceSubstring_2(self):
        solution = Solution()
        ans = "Bb"
        self.assertEqual(solution.longestNiceSubstring("Bb"), ans)
    
    def test_longestNiceSubstring_3(self):
        solution = Solution()
        ans = ""
        self.assertEqual(solution.longestNiceSubstring("c"), ans)


if __name__ == '__main__':
    unittest.main()