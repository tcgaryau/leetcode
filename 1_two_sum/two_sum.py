from typing import List


class Solution:
    """
    Brute Force
    Loops through the list twice and see if they sum up to the target
    Time Complexity O(n^2)
    Space Complexity O(1)
    """

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    """
    Two Pointers with sort
    Sort the nums in an ascending order. Then we can use two-pointers where we increment left if nums[left] + nums[right] < target and vice versa until it equals the solution
    Time Complexity O(nlogn) - this is mainly determined by the python's sorting algorithm which uses TimSort
    Space Complexity O(n) as we will have to store a sorted list
    """

    def twoSumTwoPointer(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        left_ptr, right_ptr = 0, len(nums_sorted) - 1
        while left_ptr < right_ptr:
            if nums_sorted[left_ptr] + nums_sorted[right_ptr] == target:
                break
            if nums_sorted[left_ptr] + nums_sorted[right_ptr] < target:
                left_ptr += 1
            else:
                right_ptr -= 1
        result = []
        for ind, num in enumerate(nums):
            if num == nums_sorted[left_ptr]:
                result.append(ind)
            elif num == nums_sorted[right_ptr]:
                result.append(ind)
        return result

    """
    Hash Map
    We add a hash map to track a value to the index. Then we loop through nums and if it exists in the hash map, we can return that current index and the hash map's stored index
    Time Complexity O(n)
    Space Complexity O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for ind, val in enumerate(nums):
            find_num = target - val
            if find_num in map:
                return [map[find_num], ind]
            map[val] = ind


def main():
    sol = Solution()
    test_1 = {"nums": [2, 7, 11, 15], "target": 9}
    test_2 = {"nums": [3, 2, 4], "target": 6}
    test_3 = {"nums": [3, 3], "target": 6}
    print(sol.twoSumTwoPointer(**test_1))
    print(sol.twoSumTwoPointer(**test_2))
    print(sol.twoSumTwoPointer(**test_3))


if __name__ == "__main__":
    main()
