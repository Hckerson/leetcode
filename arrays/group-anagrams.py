from typing import List
from collections import defaultdict
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for str in strs:
            grouped["".join(sorted(str))].append(str)

        return list(grouped.values())

x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
