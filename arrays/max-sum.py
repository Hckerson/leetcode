import sys


class Solution:

    def max_sum(self, arr, n, k):
        max_count = -sys.maxsize

        for i in range(n - k + 1):
            current_sum = 0
            for j in range(k):
                current_sum += arr[i + j]

            max_count = max(max_count, current_sum)

        return max_count

    def max_sum_using_slider(self, arr, n, k):
        if n < k:
            return -1

        window_sum = sum(arr[:k])

        max_sum = window_sum

        for i in range(n - k):
            window_sum = window_sum - arr[i] + arr[i + k]
            max_sum = max(max_sum, window_sum)

        return max_sum


arr = [5, 2, -1, 0, 3]
k = 3
n = len(arr)
x = Solution().max_sum(arr, n, k)
y = Solution().max_sum_using_slider(arr, n, k)
print(x)
print(y)
