from typing import *
# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
class Solution:
    # User function Template for python3
    def floorSearch(self, arr, low, high, x, result=-1):
        if low > high:
            return result

        mid = (low + high) // 2

        if arr[mid] <= x:
            return self.floorSearch(arr, mid + 1, high, x, mid)  # Move right
        else:
            return self.floorSearch(arr, low, mid - 1, x, result)  # Move left
    def findFloor(self,arr,x):
        return self.floorSearch(arr,0,len(arr)-1, x)


if __name__ =="__main__":
    bS = Solution()

    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 10
    result=bS.findFloor(arr,10)
    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")