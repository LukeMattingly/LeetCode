from typing import List
import unittest

class Solution():
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            encoded += str 
            encoded += "µ" 
        return encoded 

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        word = ""
        for letter in s:
            if letter != "µ":
                word += letter
            else:
                decoded.append(word)
                word = ""
                continue #what happens if we 'continue' but it's the last elem
        return decoded

class test_encode_decode(unittest.TestCase):
    def test_encode_decode_1(self):
        solution = Solution()
        ans = ["we","say",":","yes"]
        s1 = solution.encode(ans)
        s2 = solution.decode(s1)
        self.assertEqual(ans, s2)

    def test_canConstruct_2(self):
        solution = Solution()
        ans =  ["neet","code","love","you"]
        s1 = solution.encode(ans)
        s2 = solution.decode(s1)
        self.assertEqual(ans, s2)

if __name__ == '__main__':
    unittest.main()