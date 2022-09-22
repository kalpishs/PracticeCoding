''''
Longest palindrome substring

https://leetcode.com/problems/reverse-words-in-a-string-iii/
Date : 22-09-22
'''



from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        rev = lambda string: string[::-1]
        for i in s.split(' '):
            res += rev(i) + " "
        return res.strip()

'''
stack = []
for lt in s.split(' '):
       stack.append(lt[::-1])
return ' '.join(stack)
 '''


if __name__ =="__main__":
    solve=Solution()
    s = "Let's take LeetCode contest"
    print(solve.reverseWords(s))
    #Output: "s'teL ekat edoCteeL tsetnoc"
