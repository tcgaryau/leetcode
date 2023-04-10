from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        This solution uses 2 for loops to go through each cell on the grid once then uses DFS to determine the islands visited.
        Note, bfs can also be used here 
        Time Complexity: O(n*m)
        Space Complexity: O(n*m)
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def dfs(row, col):
            visit.add((row, col))
            for delta_row, delta_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r = row + delta_row
                c = col + delta_col
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    dfs(row, col)
                    islands += 1
        return islands

    def numIslandsBfs(self, grid: List[List[str]]) -> int:
        """
        Same solution as above but using bfs implemented iteratively
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def bfs(row, col):
            visit.add((row, col))
            queue = deque()
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    r = row + delta_row
                    c = col + delta_col
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visit:
                        visit.add((r, c))
                        queue.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row, col)
                    islands += 1
        return islands


def main():
    sol = Solution()
    test_1 = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]  # 1
    test_2 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
              ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]  # 3
    test_3 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
              ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]  # 3
    for test in [test_1, test_2, test_3]:
        print(sol.numIslands(test))


if __name__ == "__main__":
    main()
