from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Uses 2 pointer to solve
        Time Complexity O(n)
        Space Complexity O(1)
        """
        area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area


def main():
    sol = Solution()

    assert (sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
    assert (sol.maxArea([1, 1]) == 1)
    assert (sol.maxArea([1, 2]) == 1)


if __name__ == "__main__":
    main()
