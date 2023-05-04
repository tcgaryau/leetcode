from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        The key here is to track max_left and max_right of each number. 
        Then taking the min of them and subtract it from the height at each index. 
        This solution saves space complexity to O(1) by using 2 pointers instead of a list for max_right and max_left
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not height:
            return 0

        res = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res


def main():
    sol = Solution()

    assert (sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6)
    assert (sol.trap([4, 2, 0, 3, 2, 5]) == 9)
    assert (sol.trap([4, 2, 3]) == 1)


if __name__ == "__main__":
    main()
