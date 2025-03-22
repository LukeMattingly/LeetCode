import unittest
from typing import List, Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #check to see if tehre's k items, if there is, then reverse them, keep a pointer at head, and another one checks for k items
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            #reverse group
            previous = kth.next
            current = groupPrev.next
            while current != groupNext:
                temp = current.next
                current.next = previous
                previous = current
                current = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next
        
    def getKth(self, curr, k):
        while curr and k> 0:
            curr = curr.next
            k-=1
        return curr


            

         

if __name__ == '__main__':
    unittest.main()