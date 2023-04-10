class Solution:
    """
    Uses a stack to keep track of the last parenthesis to close
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isValid(self, s: str) -> bool:
        valid_brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in valid_brackets:
                stack.append(ch)
            else:
                if not stack or valid_brackets[stack.pop()] != ch:
                    return False
        return True if not stack else False


def main():
    sol = Solution()
    test_1 = "()"
    test_2 = "()[]{}"
    test_3 = "(]"
    test_4 = ""

    for test in [test_1, test_2, test_3, test_4]:
        print(sol.isValid(test))


if __name__ == "__main__":
    main()
