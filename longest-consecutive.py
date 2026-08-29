from typing import List

x = [100, 4, 200, 1, 3, 2]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_list = list(sorted(set(nums)))
        largest_count = 0
        count = 0
        if not sorted_list:
            return 0
        tracked_count = min(sorted_list)

        for num in sorted_list:
            if tracked_count != num:
                largest_count = max(largest_count, count)
                count = 0
                tracked_count = num

            count += 1
            tracked_count += 1
        largest_count = max(largest_count, count)

        return largest_count


x = Solution().longestConsecutive(x)
print(x)
