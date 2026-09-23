from typing import List

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[target - 1]:
                nums[target] = nums[i]
                target += 1

        return target


x = [-1, -1, 0, 0, 0, 1, 1, 12, 2, 3, 12]
Solution().removeDuplicates(x)
print(x)
