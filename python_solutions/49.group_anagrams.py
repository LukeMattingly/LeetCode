from typing import List
import unittest

class Solution():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        result = []

        for str in strs:
            sorted_str = sorted(str)
            tuple_sorted_str = tuple(sorted_str)
            if tuple_sorted_str not in sorted_dict:
                sorted_dict[tuple_sorted_str] = [str]
            else:
                sorted_dict[tuple_sorted_str] += [str]

        for key, values in sorted_dict.items():
            result.append(values)
            
        return result

class test_groupAnagrams(unittest.TestCase):
    def test_groupAnagrams_1(self):
        solution = Solution()
        ans = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]), ans)

    def test_groupAnagram_2(self):
        solution = Solution()
        ans = [[""]]
        self.assertEqual(solution.groupAnagrams([""]), ans)
    
    def test_groupAnagram_3(self):
        solution = Solution()
        ans = [["a"]]
        self.assertEqual(solution.groupAnagrams(["a"]), ans)

if __name__ == '__main__':
    unittest.main()