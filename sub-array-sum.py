from typing import List

x = [1, 2, 3, 2, 4]


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0: 1}

        for num in nums:
            prefix += num
            count += seen.get(prefix - k)
            seen[prefix] = seen.get(prefix, 0) + 1

        return count

solver = Solution()
print(solver.subarraySum(x, 3))
