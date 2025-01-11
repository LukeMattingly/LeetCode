from typing import List
import unittest

class Solution():
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s))+"#" + s
        
        return encoded


    def decode(self, encoded: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(encoded):
            word_len_str = ""

            while encoded[i] != "#":
                word_len_str += encoded[i]
                i += 1

            word_len_int = int(word_len_str)
            i+=1 #skip the number and the # to the next item, can't because could be double digit length. (10 lengths)

            word = ""
            for j in range(word_len_int):
                word += encoded[i]
                i+=1
            
            decoded.append(word)
        
        return decoded

            



class test_encode_decode_test(unittest.TestCase):
    def test_encode_decode_1(self):
        solution = Solution()
        ans = ["we","say",":","yes"]
        s1 = solution.encode(ans)
        s2 = solution.decode(s1)
        self.assertEqual(ans, s2)

    def test_encode_decode_2(self):
        solution = Solution()
        ans =  ["neet","code","love","you"]
        s1 = solution.encode(ans)
        s2 = solution.decode(s1)
        self.assertEqual(ans, s2)

    def test_encode_decode_3(self):
        solution = Solution()
        ans =  ["we","say",":","yes","!@#$%^&*()"]
        s1 = solution.encode(ans)
        s2 = solution.decode(s1)
        self.assertEqual(ans, s2)

if __name__ == '__main__':
    unittest.main()