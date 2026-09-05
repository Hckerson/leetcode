from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        store = {}

        for i in range(len(nums)):
            if store.get(nums[i]) is None:
                store[nums[i]] = nums[i]
            else:
                return True
        return False
