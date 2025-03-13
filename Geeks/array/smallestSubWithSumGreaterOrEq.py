#https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign
from typing import *

class Solution:
    @staticmethod
    def smallestSubWithSum(x:int, arr:list[int]):
        high, low = 0, 0
        sum = 0
        result = float('inf')
        n = len(arr)
        while high < n:
            sum += arr[high]
            while sum > x:
                result = min(result, high - low + 1)
                sum -= arr[low]
                low += 1
            high += 1
        if result == float('inf'):
            return 0
        return result
        # Your code goes here





if __name__ =="__main__":
    bS = Solution()
    inputArr:list[int] = [2, 3, 4, 10, 40]
    numberX:int = 55
    result=bS.smallestSubWithSum(numberX,inputArr)
    print(f"size of the smallest sub arr with sum >= {numberX} is {result}")
