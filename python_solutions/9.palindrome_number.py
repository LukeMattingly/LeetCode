import unittest

class Solution():
    def isPalindrome(self, x:int)-> bool:
        if(str(x) == str(x)[::-1]):
            return True
        return False
    
class testIsPalindrome(unittest.TestCase):
    def test_isPalindrome_1(self):
        solution = Solution()
        ans = True
        self.assertEqual(solution.isPalindrome(131), ans)

    def test_isPalindrome_2(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.isPalindrome(-121), ans)

    def test_isPalindrome_3(self):
        solution = Solution()
        ans = False
        self.assertEqual(solution.isPalindrome(10), ans)

#Solve without converting to a string
class Solution2():
    def isPalindrome(self, x:int)-> bool:
        digits = []
        if x < 0:
            return False

        while x > 0:
            d = x % 10 #extract rightmost digit using modulo
            digits.append(d)
            x //= 10 #remove the rightmove digit using integer division
        
        if digits == digits[::-1]:
            return True
        else:
            return False

class testIsPalindrome2(unittest.TestCase):
    def test_isPalindrome_1(self):
        solution = Solution2()
        ans = True
        self.assertEqual(solution.isPalindrome(131), ans)

    def test_isPalindrome_2(self):
        solution = Solution2()
        ans = False
        self.assertEqual(solution.isPalindrome(-121), ans)

    def test_isPalindrome_3(self):
        solution = Solution2()
        ans = False
        self.assertEqual(solution.isPalindrome(10), ans)

         

if __name__ == '__main__':
    unittest.main()
