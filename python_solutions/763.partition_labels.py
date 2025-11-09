from typing import List
import unittest
from collections import defaultdict

class Solution():
    def partitionLabels(self, s: str) -> List[int]:
        letter_map = defaultdict(list)

        for i, char in enumerate(s):
            if char in letter_map:
                letter_map[char][1] = i #update end
            else:
                letter_map[char] = [i,i]

        res = []

        intervals = sorted(letter_map.values(), key=lambda x:x[0])

        curr_start, curr_end = intervals[0]  # start with first

        for start, end in intervals:
            if start <= curr_end:
                curr_end = max(curr_end, end)
            else: #dont overlap
                res.append(curr_end - curr_start +1)
                curr_start, curr_end = start, end
            
        res.append(curr_end - curr_start +1)
        return res


if __name__ == '__main__':
    unittest.main()