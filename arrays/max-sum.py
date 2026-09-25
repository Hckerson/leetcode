import sys

"""
Learnt Sliding window technique here

"""


class Solution:
    def max_sum_using_slider(self, arr, n, k):
        if n < k:
            return -1

        window_count = sum(arr[:k])

        for i in range(n - k):
            recomputed_value = window_count - arr[i] + arr[i + k]
            window_count = max(window_count, recomputed_value)

        return window_count


arr = [5, 2, -1, 0, 3]
k = 3
n = len(arr)
y = Solution().max_sum_using_slider(arr, n, k)
print(y)
