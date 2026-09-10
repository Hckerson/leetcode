from typing import List

x = [2, 9, 0, 2]


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0: 1}

        for num in nums:
            prefix += num
            count += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1

        return count

solver = Solution()
print(solver.subarraySum(x, 2))
