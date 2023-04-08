from typing import List

"""
From the pingeonhole principle, we know that there contains a n + 1 amount of integers in the range [1, n] inclusive which means there has to contain a duplicate.
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        We know this contains a cycle since there is a duplicate number. This means floyd's cycle detection algorithm would work here and the start of the loop would be the duplicate number.
        Time Complexity O(n)
        Space Complexity O(1)
        """
        tortoise, hare = 0, 0

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        start = 0
        while start != hare:
            start = nums[start]
            hare = nums[hare]
            if start == hare:
                return start
        return -1


def main():
    sol = Solution()
    test_1 = [1, 3, 4, 2, 2]  # 2
    test_2 = [3, 1, 3, 4, 2]  # 3
    for test in [test_1, test_2]:
        print(sol.findDuplicate(test))


if __name__ == "__main__":
    main()
