from typing import List


class Solution:
    """
    Brute Force
    Loops through and check every value against every other value and see if they match.
    Time Complexity O(n^2)
    Space Complexity O(1)
    """

    def contains_duplicate_brute_force(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    """
    Sorting
    Sorts the list and loops through the nums once checking every neighbor to see if they match.
    Time Complexity O(nlogn)
    Space Complexity O(1)
    """

    def contains_duplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    """
    Uses a set to store the values and check if the value is already in the set.
    Time Complexity O(n)
    Space Complexity O(n)
    """

    def contains_duplicate_set(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False

    """
    Uses set as well but comparing the lengths of the set vs the list
    Time Complexity O(n)
    Space Complexity O(n)
    """

    def contains_duplicate_set_len(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


def main():
    sol = Solution()
    test_1 = [1, 2, 3, 1]
    test_2 = [1, 2, 3, 4]
    test_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(sol.contains_duplicate_set(test_1))  # true
    print(sol.contains_duplicate_set(test_2))  # false
    print(sol.contains_duplicate_set(test_3))  # true


if __name__ == "__main__":
    main()
