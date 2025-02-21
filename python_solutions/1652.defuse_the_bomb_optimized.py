from typing import List
import unittest


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0]*n            

        if k == 0:
            return result

        l = 0
        curr_sum = 0
        for r in range(n+abs(k)):
            curr_sum += code[r %n]

            if r - l + 1 > abs(k):
                curr_sum -=  code[l % n]
                l = (l + 1 ) %n

            if r - l +1 == abs(k):
                if k > 0:
                    result[(l-1)%n] = curr_sum
                elif k < 0:
                    result[(r+1)%n] = curr_sum

        return result

        
    
class test_decrypt(unittest.TestCase):
    def test_decrypt_1(self):
        solution = Solution()
        ans = [12,10,16,13]
        self.assertEqual(solution.decrypt([5,7,1,4], 3), ans)

    def test_decrypt_2(self):
        solution = Solution()
        ans = [0,0,0,0]
        self.assertEqual(solution.decrypt([1,2,3,4],0), ans)
    
    def test_decrypt_3(self):
        solution = Solution()
        ans = [12,5,6,13]
        self.assertEqual(solution.decrypt([2,4,9,3],-2), ans)


if __name__ == '__main__':
    unittest.main()