from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        if len(strs) < 1: return groups

        for word in strs:
            sorted_char = "".join(sorted(word))
            groups.setdefault(sorted_char, []).append(word)
        return list(groups.values())


x = Solution()
print(x.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))