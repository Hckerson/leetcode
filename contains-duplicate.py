from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            if len == 1:
                return False
            if len == 2:
                return nums[0] == nums[1]
        store = {}

        for i in range(len(nums)):
            if store.get(nums[i]) is None:
                store[nums[i]] = nums[i]
            else:
                return True
        return False
