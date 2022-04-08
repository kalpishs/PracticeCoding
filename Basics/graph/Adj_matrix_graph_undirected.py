from typing import *
class Solution:
    def build_graph(self,m,k):
        arr=[([0]*m) for i in range(m)]
        for i in range(k):
            row_col=input("Enter valid eg: vertex M {0,1,2} valid N {0,1,2} for 3*3 ").split()
            arr[int(row_col[0])][int(row_col[1])]=1
            arr[int(row_col[1])][int(row_col[0])]=1
        return arr


if __name__ == "__main__":
    solve = Solution()
    print(f"output {solve.build_graph(5,7)}")
