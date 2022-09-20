''''
Longest palindrome substring

https://leetcode.com/problems/find-duplicate-file-in-system/
Date : 20-sept-2022
'''
from typing import *
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        index =0
        dict_res ={}
        result = []
        for x in paths:
            files = x.split(' ')
            for y in range(1,len(files)):
                t = files[y].split('(')
                name=files[0]+"/"+t[0]
                content=t[1][:-1]
                if content in dict_res:
                    #add the index from dict and append the name to that result eg: dict is  {'abcd': 0, 'efgh': 1} then for content abcd it gets appended to result[0] and efgh gets appended to result[1]
                    #append name will add path till name eg:root/c/d/4.txt
                    result[dict_res[content]].append(name)
                else:
                    result.append([name])
                    dict_res[content] = index
                    index+=1
        final_res=[]
        for x in result:
            if len(x) >=2:
                final_res.append(x)
        return final_res

if __name__=="__main__":
    solve = Solution()
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    print(solve.findDuplicate(paths))