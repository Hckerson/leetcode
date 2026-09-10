class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        store = {}

        for char in s:
            store[char] = store.get(char, 0) + 1

        for char in t:
            if char not in store:
                return False
            store[char] -= 1
            if store[char] == 0:
                del store[char]

        return not store


x = Solution()
print(x.isAnagram("anagram", "nagaram"))
