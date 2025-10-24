from typing import List
import unittest


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        times_map = {}
        res =[]

        for access_time in access_times:
            user, time = access_time
            if user in times_map:
                times_map[user].append(time)
            else:
                times_map[user] = []
                times_map[user].append(time)
            
        for key, value in times_map.items():
            sorted_value = sorted(value)
            for i in range(len(sorted_value)-2):
                startTime = sorted_value[i]
                endTime = sorted_value[i+2]

                if self.calcMinutes(endTime) - self.calcMinutes(startTime) < 60:
                    res.append(key)
                    break

        return res

    def calcMinutes(self,time: str) -> int:
        #need split string into hh and mm
        hours = time[0:2]
        minutes = time[2:4] 
        return int(hours) * 60 + int(minutes)
