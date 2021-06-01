''''
Encode and Decode Strings

https://leetcode.com/problems/count-and-say/

 '''

from typing import *

class Solution:
    def say_num(self, num: str):
        result = ''
        str_n = str(num)
        prev = str_n[0]
        count = 1
        for i in range(1, len(str_n)):
            if str_n[i] == prev:
                count += 1
            else:
                result += str(count) + prev
                count = 1
            prev = str_n[i]
        result += str(count) + prev
        return result

    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return '1'
        if (n == 2):
            return '11'
        s = '11'
        for i in range(3, n + 1):
            res = self.say_num(s)
            s=res
        return s

if __name__ == "__main__":
    solve = Solution()
    print(solve.countAndSay(4))