from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = {}
        freq = (nums[0], 0)

        for num in nums:
            new_count = store.get(num, 0) + 1
            store[num] = new_count

            if new_count > freq[1]:
                freq = (num, new_count)

        return freq[0]
