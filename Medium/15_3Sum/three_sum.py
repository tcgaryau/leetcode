from typing import List


class Solution:
    """
    Sort the nums first. Then we loop through nums and then put in a 2-pointer solution from two-sum to determine if we need to add it to our results.
    Time Complexity: O(n^2) - because sorting is O(nlogn) and looping through it twice is O(n^2)
    Space Complexity: O(n) since python uses Timsort which is a variation of merge sort.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


def main():
    sol = Solution()
    test_1 = [-1, 0, 1, 2, -1, -4]
    test_2 = [0, 1, 1]
    test_3 = [0, 0, 0]
    for test in [test_1, test_2, test_3]:
        print(sol.threeSum(test))


if __name__ == "__main__":
    main()
