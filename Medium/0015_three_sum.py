from typing import List


class Solution:
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force approach using 3 pointers to iterate through the list. It sorts the nums list first.
        Time Complexity: O(n^3)
        Space Complexity: O(1)
        """
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res

    def threeSumBinarySearch(self, nums: List[int]) -> List[List[int]]:
        """
        Make 2 pointers that iterate it from i to N-1 and j=i+1 to N-1 and iterate through it. The last value we can use a binary search on the remaining subtree for - (nums[i] + nums[j])
        and if it exists, we can return it.
        Time Complexity: O(n^2 log(n))
        Space Complexity: O(1) if we don't count the result array
        """
        def binarySearch(low, high, target, nums) -> bool:
            if low > high:
                return False
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                return binarySearch(low, mid - 1, target, nums)
            else:
                return binarySearch(mid + 1, high, target, nums)

        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if binarySearch(j+1, len(nums) - 1, target, nums):
                    res.append([nums[i], nums[j], target])
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort the nums first. Then we loop through nums and then put in a 2-pointer solution from two-sum to determine if we need to add it to our results.
        Time Complexity: O(n^2) - because sorting is O(nlogn) and looping through it twice is O(n^2)
        Space Complexity: O(n) since python uses Timsort which is a variation of merge sort.
        """
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
    test_1 = [-1, 0, 1, 2, -1, -4]  # [[-1, -1, 2], [-1, 0, 1]]
    test_2 = [0, 1, 1]  # []
    test_3 = [0, 0, 0]  # [[0,0,0]]
    for test in [test_1, test_2, test_3]:
        print(sol.threeSumBinarySearch(test))


if __name__ == "__main__":
    main()
