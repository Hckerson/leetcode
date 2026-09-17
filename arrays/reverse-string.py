from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        first, last = 0, len(s) - 1

        while first < last:
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1


s = list("struct")
x = Solution().reverseString(s)
print("".join(s))
