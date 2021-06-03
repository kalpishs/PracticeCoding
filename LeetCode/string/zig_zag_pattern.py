"""
https://leetcode.com/problems/zigzag-conversion/

Input: str= PAYPALISHIRING , n=3
Explanation: Let us write input string in Zig-Zag fashion (mountain)
             in 3 rows.
P       A       H       N
  A   P   L   S   I   I   G
    Y       I       R
OUTPUT: PAHNAPLSIIGYIR
"""
from typing import *
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        current_row=1
        dir_down=True
        output_arr=['' for i in range(numRows)]
        len_s=len(s)
        output_arr[0]=s[0]
        for i in range(1,len_s):
            output_arr[current_row]+=s[i]
            if current_row == numRows-1 or current_row==0:
                dir_down^=True
            if(dir_down):
                current_row+=1
            else:
                current_row-=1
        return ''.join(output_arr)

if __name__=="__main__":
    solve = Solution()
    print(solve.convert('AB',1))



