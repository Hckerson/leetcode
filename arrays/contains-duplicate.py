from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        store = {}

        for num in nums:
            if store.get(num) is None:
                store[num] = num
            else:
                return True
        return False
