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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #two pointers a previous and a current one
        previous = None
        current = head #need to start move pointer(current) to the current head

        while current:
            temp = current.next #save off the next pointer 
            current.next = previous #overwrite the next pointer to teh previous value you saved

            previous = current #update for next iteration
            current = temp #update current to the saved current.next pointer before you overwrote it

        return previous 


if __name__ == '__main__':
    unittest.main()
