from typing import List

"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], idx]
            store[num] = idx
        return []


x = Solution()
answer = x.twoSum([2, 3, 4], 6)
print(answer)
