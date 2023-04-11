from typing import List


class Solution:
    def countBitsBruteForce(self, n: int) -> List[int]:
        """
        This is a brute force approach where it counts the # of 1's for every number in the loop
        Time Complexity: O(nlogn)
        Space Complexity: O(n) 
        """
        def hammingWeight(num):
            weight = 0
            while num:
                weight += num % 2
                num = num >> 1
            return weight
        ans = []
        for i in range(n + 1):
            ans.append(hammingWeight(i))
        return ans

    def countBits(self, n: int) -> List[int]:
        """
        This approach is using dynamic programming and the idea that if we bit shift it by 1, we can get that results from the dp array and then determine if we need to add a 1 or 0 to it
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


def main():
    sol = Solution()
    test_1 = 2  # [0, 1, 1]
    test_2 = 5  # [0, 1, 1, 2, 1, 2]
    for test in [test_1, test_2]:
        print(sol.countBits(test))


if __name__ == "__main__":
    main()
