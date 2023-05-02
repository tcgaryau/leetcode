from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(num_open, num_close):
            if num_open == num_close == n:
                result.append("".join(stack))
                return

            if num_open < n:
                stack.append("(")
                backtrack(num_open + 1, num_close)
                stack.pop()
            if num_close < num_open:
                stack.append(")")
                backtrack(num_open, num_close + 1)
                stack.pop()

        backtrack(0, 0)
        return result


def main():
    sol = Solution()
    assert (sol.generateParenthesis(3) ==
            ["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert (sol.generateParenthesis(1) == ["()"])


if __name__ == "__main__":
    main()
