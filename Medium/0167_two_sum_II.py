from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum < target:
                left += 1
            else:
                right -= 1

        return None


def main():
    sol = Solution()
    assert (sol.twoSum([[2, 7, 11, 15]] == [1, 2]))
    assert (sol.twoSum([[2, 3, 4]]) == [1, 3])
    assert (sol.twoSum([-1, 0]) == [1, 2])


if __name__ == "__main__":
    main()
