import unittest

class Solution():
    def intToRoman(self, num:int)->str:
        ruleDict = {
                1000: 'M',
                900: 'CM',
                500: 'D',
                400: 'CD',
                100: 'C',
                90: 'XC',
                50: 'L',
                40: 'XL',
                10: 'X',
                9: 'IX', 
                5: 'V',
                4: 'IV',
                1: 'I',
        }

        res = []

        for key, value in ruleDict.items():
           rem = num //key
           if rem > 0:
               res.append(value * rem)
               num -= rem * key
        return "".join(res)

class testSolution(unittest.TestCase):
    def test_intToRoman_1(self):
        solution = Solution()
        ans = 'III'
        self.assertEqual(solution.intToRoman(3), ans)
    def test_intToRoman_2(self):
        solution = Solution()
        ans = 'LVIII'
        self.assertEqual(solution.intToRoman(58), ans)
    def test_intToRoman_3(self):
        solution = Solution()
        ans = 'MCMXCIV'
        self.assertEqual(solution.intToRoman(1994), ans)


if __name__ =='__main__':
    unittest.main()
