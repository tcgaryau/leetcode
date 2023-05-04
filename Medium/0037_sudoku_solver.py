from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        This solution uses a list of sets on its rows, columns, and sub_grid and checks if a cell has a value in the corresponding row, column, or sub_grid then it won't be a valid sudoku
        Time Complexity: O(n * m) -> since n = m O(n^2)
        Space Complexity: O(n)
        """
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        sub_grid = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rows[row] or val in cols[col] or val in sub_grid[3 * (row // 3) + col // 3]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                sub_grid[3 * (row // 3) + col // 3].add(val)
        return True


def main():
    sol = Solution()
    board_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert (sol.isValidSudoku(board_1) == True)

    board_2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert (sol.isValidSudoku(board_2) == False)


if __name__ == "__main__":
    main()
