# https://practice.geeksforgeeks.org/problems/gold-mine-problem/0
# code
from typing import *

class Goldmine:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        gold_mine = [[0 for i in range(n)] for j in range(m)]
        for col in range(n - 1, -1, -1):
            for row in range(m):
                # check the condition when its last column
                if col == n - 1:
                    right = 0
                else:
                    right = gold_mine[row][col + 1]
                # check the condition when its last row or last column
                if row == m - 1 or col == n - 1:
                    right_down = 0
                else:
                    right_down = gold_mine[row + 1][col + 1]
                # check the condition when its First row or last column
                if row == 0 or col == n - 1:
                    right_up = 0
                else:
                    right_up = gold_mine[row - 1][col + 1]

                gold_mine[row][col] = grid[row][col] + max(right, right_up, right_down)
        result = 0
        for i in range(n):
            result = max(result, gold_mine[i][0])
        return result


if __name__ == '__main__':
    t = input()
    for test in range(int(t)):
        row, col = [int(x) for x in input().split()]
        list_val = [int(x) for x in input().split()]
        grid = []
        init = 0
        col_init = col
        for i in range(row):
            grid.append(list_val[init:col_init])
            init = col_init
            col_init += col
        print(Goldmine().getMaximumGold(grid))