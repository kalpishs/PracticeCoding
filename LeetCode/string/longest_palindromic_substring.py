from typing import *
class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        arr= [ ([0] * len_s) for row in range(len_s) ]
        arr[0][0] = 1
        start,end=0,0
        len_max=1
        for i in range(len_s):
            arr[i][i]=1
            if i <len_s-1 and s[i] == s[i+1]:
                arr[i][i+1]=1
                start,end=i,i+1
                len_max=2
        for k in range(3,len_s+1):
            for i in range(0, len_s - k +1) :
                j= i + k -1
                if s[i] == s[j] and arr[i + 1][j - 1] == 1:
                    arr[i][j] = 1
                    if k > len_max:
                        len_max = k
                        start = i
                        end=j
        #print(start,end)
        return s[start:end+1]



if __name__ =="__main__":
    solve=Solution()
    print(solve.longestPalindrome('aaaaa'))