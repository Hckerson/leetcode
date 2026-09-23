from typing import List

x = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_list = list(sorted(set(nums)))
        largest_count = 0
        count = 1
        if not sorted_list:
            return 0

        start = sorted_list[0]
        for num in sorted_list:
            if num != start + 1:
                if num == start:
                    continue
                start = num
                largest_count = max(count, largest_count)
                count = 1
                continue
            start += 1
            count += 1

        largest_count = max(largest_count, count)
        return largest_count


x = Solution().longestConsecutive(x)
print(x)
