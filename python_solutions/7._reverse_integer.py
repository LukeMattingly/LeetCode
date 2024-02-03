import unittest

class Solution:
    def reverse(self, x: int) -> int:
        if x==0: return 0
        if x < 0: 
            res = -int(str(x)[1:][::-1])
            if res < -2**31:
                return 0
            return res
        if x > 0:
            res = int(str(x)[::-1])
            if res > 2**31:
                return 0
            return res


class testAddTwoNumbers(unittest.TestCase):
    def test_reverse_1(self):
        solution = Solution()
        ans = 321
        self.assertEqual(solution.reverse(123), ans)

    def test_reverse_2(self):
        solution = Solution()
        ans = -321
        self.assertEqual(solution.reverse(-123), ans)
    
    def test_reverse_3(self):
        solution = Solution()
        ans = 21
        self.assertEqual(solution.reverse(120), ans)

    def test_reverse_4(self):
        solution = Solution()
        ans = 0
        self.assertEqual(solution.reverse(1534236469), ans)
    


if __name__ == '__main__':
    unittest.main()
