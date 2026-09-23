from typing import List

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:

    def moveZeroesSwap(self, nums: List[int]) -> None:
        insert = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1


y = [0, 1, 0, 3, 12]
Solution().moveZeroes(y)
print(y)
