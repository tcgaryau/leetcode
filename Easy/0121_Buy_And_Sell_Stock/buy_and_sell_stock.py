from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Two Pointer solutions and we use this to find the local max. Left pointer is moved to right pointer if the price at right is lower than left.
        Time Complexity O(n) - loop through the list once
        Space Complexity O(1)
        """
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            profit = max(profit, prices[r] - prices[l])
            r += 1
        return profit


def main():
    sol = Solution()
    test_1 = [7, 1, 5, 3, 6, 4]
    test_2 = [7, 4, 3, 1]
    print(sol.maxProfit(test_1))  # 5
    print(sol.maxProfit(test_2))  # 0


if __name__ == "__main__":
    main()
