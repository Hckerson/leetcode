from typing import List


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
