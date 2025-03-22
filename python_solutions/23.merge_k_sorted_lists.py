import unittest
from typing import List, Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2): #doign pairs of linked lists so pairs of 2
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None #so we handle the last list when we have an odd number
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists #keep updated lists until we just have finally merged list
        return lists[0]

    def mergeLists(self, l1, l2):
        temp = ListNode()
        curr = temp
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        #once you finish with one list that means you can short circuit and just append all of the rest of the other one
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return temp.next
            

         

if __name__ == '__main__':
    unittest.main()