from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        tracker = [[0] * 11 for _ in range(n)]
        winners = set()
        for player, ball in pick:
            tracker[player][ball] += 1
            if tracker[player][ball] > player:
                winners.add(player)

        return len(winners)


x = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]
y = Solution().winningPlayerCount(4, x)
print(y)
