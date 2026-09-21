from typing import List
from collections import Counter

"""
Return true if the frequency of any element of the array is prime,
otherwise, return false.
"""

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for d in range(2, int(n ** 0.5) + 1):
                if n % d == 0:
                    return False
            return True

        return any(is_prime(count) for count in Counter(nums).values())


y = [1,2,3,4,5,4]
x = Solution().checkPrimeFrequency(y)
print(x)
