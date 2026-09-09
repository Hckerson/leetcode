from typing import List

x = [9, 0, 2]


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0: 1}

        print(f"nums = {nums}, k = {k}")
        print(f"seed   seen={seen}  <- the empty prefix\n")

        for num in nums:
            prefix += num
            print(f"num={num:>3}  prefix={prefix:>3}  need prefix-k={prefix - k:>3}  found {seen.get(prefix - k, 0)}")

            count += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
            print(f"          count={count}  seen={seen}\n")

        print(f"result = {count}")
        return count


solver = Solution()
print(solver.subarraySum(x, 2))
