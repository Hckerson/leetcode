from typing import List

x = [3, 4, 5, 3, 4]

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tracker = {}

        for num in nums: 
            tracker[num] = tracker.get(num, 0) + 1

        return sorted(tracker,key=tracker.get, reverse=True)[:k]


y= Solution().topKFrequent(x, 2)
print(y)