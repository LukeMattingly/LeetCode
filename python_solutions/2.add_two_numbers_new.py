from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        # Compare the values of the current node
        if self.val != other.val:
            return False

        # Recursively compare the next nodes
        if self.next is None and other.next is None:
            return True
        elif self.next is None or other.next is None:
            return False
        else:
            return self.next == other.next

     def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            res = v1 + v2 + carry
            carry = res // 10
            res = res % 10 
            curr.next = ListNode(res)

            #update pointers
            curr = curr. next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


class testAddTwoNumbers(unittest.TestCase):
    def test_addTwoNumbers_1(self):
        solution = Solution()
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        ans = ListNode(7, ListNode(0, ListNode(8)))
        self.assertEqual(solution.addTwoNumbers(l1, l2), ans)
    
    def test_addTwoNumbers_2(self):
        solution = Solution()
        l1 = ListNode(0)
        l2 = ListNode(0)
        ans = ListNode(0)
        self.assertEqual(solution.addTwoNumbers(l1, l2), ans)
    
    def test_addTwoNumbers_3(self):
        solution = Solution()
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        ans = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
        self.assertEqual(solution.addTwoNumbers(l1, l2), ans)


if __name__ == '__main__':
    unittest.main()