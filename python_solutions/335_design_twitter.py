from typing import List, Optional, Deque
import unittest
from collections import defaultdict
import heapq 

class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -=1
        self.tweetMap[userId].append([self.count,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []

        self.followMap[userId].add(userId)
        for followerId in self.followMap[userId]:
            if followerId in self.tweetMap:
                index = len(self.tweetMap[followerId])-1
                count, tweetId = self.tweetMap[followerId][index]
                minHeap.append([count,tweetId, followerId, index-1])
        
        heapq.heapify(minHeap)
        while minHeap and len(res) <10:
            count, tweetId, followerId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >=0:
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(minHeap, [count, tweetId, followerId, index -1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
            


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)