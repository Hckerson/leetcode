"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s)).lower()
        return cleaned == cleaned[::-1]

    def isPalindromeTwoPointer(self, s: str) -> bool:
        start, stop = 0, len(s) - 1
        while start < stop:
            while start < stop and not s[start].isalnum():
                start += 1
            while start < stop and not s[stop].isalnum():
                stop -= 1
            if s[start].lower() != s[stop].lower():
                return False
            start += 1
            stop -= 1
        return True


x = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(x)
