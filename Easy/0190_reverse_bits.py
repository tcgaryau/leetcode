class Solution:
    def reverseBits(self, n: int) -> int:
        """
        To find the last digit, we can bitwise and with 1 to determine if its 1 or 0
        Then we just need a loop to shift it for every bit
        For the result, since it is in reverse we can shift it by 31 - i and bitwise or the bit we found above.
        Time Complexity: O(1) since it always loops 32 times
        Space Complexity: O(1) since we're only keeping track of an integer
        """
        reverse = 0
        for i in range(32):
            bit = (n >> i) & 1
            reverse = reverse | bit << (31 - i)
        return reverse


def main():
    sol = Solution()
    # return 964176192 which its binary representation is 00111001011110000010100101000000
    test_1 = 0b00000010100101000001111010011100
    # return 3221225471 which its binary representation is 10111111111111111111111111111111
    test_2 = 0b11111111111111111111111111111101
    for test in [test_1, test_2]:
        print(sol.reverseBits(test))


if __name__ == "__main__":
    main()
