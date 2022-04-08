"""https://leetcode.com/problems/reshape-the-matrix/"""
from typing import *
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat[0]) * len(mat) != r*c:
            return mat
        elif len(mat) == r and len(mat[0]) == c:
            return mat
        
        arr =  []
        counter=c
        temp=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if counter > 0:
                    temp.append(mat[i][j])
                    counter=counter-1
                    if counter==0:
                        arr.append(temp)
                        temp=[]
                        counter=c
        return arr



if __name__ == "__main__":
    solve = Solution()
    print(f"output {solve.matrixReshape([[1],[2],[3],[4]],1,4)}")
