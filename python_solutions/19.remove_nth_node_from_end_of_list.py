from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = head
        n_behind= dummy

        while n>0 and current:
            current = current.next
            #wait n valuves
            n -=1

        while current:
            current = current.next
            n_behind = n_behind.next

        n_behind.next = n_behind.next.next
        
        return dummy.next


class test_removeNthFromEnd(unittest.TestCase):
    def test_removeNthFromEnd_1(self):
        solution = Solution()
        ans = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(solution.removeNthFromEnd("23"), ans)

    def test_removeNthFromEnd_2(self):
        solution = Solution()
        ans = []
        self.assertEqual(solution.removeNthFromEnd(""), ans)

    def test_removeNthFromEnd_3(self):
        solution = Solution()
        ans = ["a","b","c"]
        self.assertEqual(solution.removeNthFromEnd("2"), ans)


         

if __name__ == '__main__':
    unittest.main()
