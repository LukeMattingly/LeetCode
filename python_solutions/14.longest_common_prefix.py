from typing import List
import unittest

class Solution():
    def longestCommonPrefix(self, strs: List[str])-> str:
        if len(strs) == 1:
            return strs[0]
        currentLongest = []
        for i in range(len(strs[0])):
            for str in strs:
                if i==len(str) or str[i] != strs[0][i]:
                    return "".join(currentLongest)
            currentLongest.append(strs[0][i])
                
        return "".join(currentLongest)


class test_longestCommonPrefix(unittest.TestCase):
    def test_longestCommonPrefix_1(self):
        solution = Solution()
        ans = "fl"
        self.assertEqual(solution.longestCommonPrefix(["flower","flow","flight"]), ans)

    def test_longestCommonPrefix_2(self):
        solution = Solution()
        ans = ""
        self.assertEqual(solution.longestCommonPrefix(["dog","racecar","car"]), ans)

    def test_longestCommonPrefix_3(self):
        solution = Solution()
        ans = "flower"
        self.assertEqual(solution.longestCommonPrefix(["flower","flowers","flowering"]), ans)

if __name__ == '__main__':
    unittest.main()