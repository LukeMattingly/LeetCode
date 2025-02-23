from typing import List
import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        count = {} #dict keeps track of letter freq in the window range

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # dict key is value of current postion in string, get with 2nd pos as 0 is default if it doesnt exist
            
            #current window is right - left +1
            while (r - l + 1) - max(count.values()) > k: #max(count.values()) goes through the dict and finds the largest value 
                count[s[l]] -=1 #if we have to advance teh left pointer then we need to decrement it from the dict 
                l+=1


            max_length = max(max_length, r - l + 1) #current window is right - left +1
            
        return max_length


#O(n * 26) bc count is max len of 26 and we have to go through it 
        
    
class test_characterReplacement(unittest.TestCase):
    def test_characterReplacement_1(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.characterReplacement("ABAB", 2), ans)

    def test_characterReplacement_2(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.characterReplacement("AABABBA",1), ans)
    
    def test_characterReplacement_3(self):
        solution = Solution()
        ans = 4
        self.assertEqual(solution.characterReplacement("XYYX",2), ans)

    def test_characterReplacement_4(self):
        solution = Solution()
        ans = 5
        self.assertEqual(solution.characterReplacement("AAABABB",1), ans)



if __name__ == '__main__':
    unittest.main()