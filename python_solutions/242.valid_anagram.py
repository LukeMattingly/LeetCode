from typing import List
import unittest

class Solution():
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}
        for i in s:
            if i in char_count:
                char_count[i] +=1
            else:
                char_count[i] = 1
        
        for j in t:
            if j in char_count:
                char_count[j] -=1
            else:
                return False #value isn't found in dict

        for key in char_count:
            if char_count[key] != 0:
                return False

        return True



class test_isAnagram_test(unittest.TestCase):
    def test_isAnagram_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.isAnagram("anagram", "nagaram" ), ans)

    def test_isAnagram_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.isAnagram("rat", "car" ), ans)

if __name__ == '__main__':
    unittest.main()