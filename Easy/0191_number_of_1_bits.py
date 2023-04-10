class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        We know that even number would always have 0 and odd is 1 at the last digit in binary, so we loop over the number and bit shift the number until it is 0
        Time Complexity: O(1) since n is length 32
        Space Complexity: O(1)
        """
        hamming_distance = 0
        while n:
            hamming_distance += n % 2
            n = n >> 1
        return hamming_distance


def main():
    sol = Solution()
    test_1 = 0b00000000000000000000000000001011  # 3
    test_2 = 0b00000000000000000000000010000000  # 1
    test_3 = 0b11111111111111111111111111111101  # 31
    for test in [test_1, test_2, test_3]:
        print(sol.hammingWeight(test))


if __name__ == "__main__":
    main()
