from typing import List

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        store = {}

        for num in nums:
            if store.get(num) is None:
                store[num] = num
            else:
                return True
        return False
