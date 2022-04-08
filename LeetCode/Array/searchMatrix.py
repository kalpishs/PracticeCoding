"""
Leetcode 2D sorded matrix
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

[[10, 20, 30, 40]
[15, 25, 35, 45]
[28, 29, 37, 49]
[33, 34, 38, 50]]
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
from typing import *
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_bound=0
        col_bound=len(matrix[0])-1
        while row_bound < len(matrix) and col_bound >= 0:
            if (matrix[row_bound][col_bound] == target):
                return True
            elif matrix[row_bound][col_bound] > target:
                col_bound=col_bound-1
            elif matrix[row_bound][col_bound] < target:
                row_bound=row_bound+1
        return False
        pass

if __name__ == "__main__":
    solve = Solution()
    print(f"output {solve.searchMatrix([[10,20,30,40],[15,25,35,45],[28,29,37,49],[33,34,38,50]],50)}")