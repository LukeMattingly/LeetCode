from typing import Optional
import unittest

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(current, previous):
            if current is None:
                return previous
            else:
                next = current.next
                current.next = previous
                return reverse(next, current)
        
        return reverse(head, None)


class test_twoSum(unittest.TestCase):
    def test_twoSum_1(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.twoSum([2,7,11,15], 9), ans)

    def test_twoSum_2(self):
        solution = Solution()
        ans = [1,3]
        self.assertEqual(solution.twoSum([2,3,4], 6), ans)

    def test_twoSum_3(self):
        solution = Solution()
        ans = [1,2]
        self.assertEqual(solution.twoSum([-1,0], -1), ans)


if __name__ == '__main__':
    unittest.main()
