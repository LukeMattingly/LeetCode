import unittest
from typing import List
import heapq 
from collections import Counter, defaultdict, deque

class Solution:
        def leastInterval(self, tasks: List[str], n: int) -> int:
            freq_count = Counter(tasks)
            max_heap = [-cnt for cnt in freq_count.values()]
            heapq.heapify(max_heap)

            total_time =0
            cooldown = deque() # pairs of [-cnt, idle_time]

            while max_heap or cooldown:
                 total_time+=1

                 if max_heap:
                      cnt = 1+ heapq.heappop(max_heap) #since our max heap contains negatives we add one to decrement the total
                      if cnt:
                            cooldown.append([cnt, total_time+n])
                 
                 if cooldown and cooldown[0][1] == total_time:
                      heapq.heappush(max_heap, cooldown.popleft()[0])

            return total_time     
                    

        
class test_leastInterval(unittest.TestCase):
    def test_leastInterval_1(self):
        solution = Solution()
        ans = 5
        self.assertEqual(solution.leastInterval(["X","X","Y","Y"], 2), ans)

    def test_leastInterval_2(self):
        solution = Solution()
        ans = 9
        self.assertEqual(solution.leastInterval(["A","A","A","B","C"],3), ans)
    

if __name__ == '__main__':
    unittest.main()
