# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

"""https://leetcode.com/problems/find-in-mountain-array/"""
class MountainArray:
    def __init__(self):
        self._arr = []

    def get(self, index: int) -> int:
        return self._arr[index]

    def length(self) -> int:
        return len(self._arr)

    def arr(self, a):
        self._arr = a


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        low = 1
        length = mountainArr.length()
        high = length - 2
        while low < high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak = low

        # search in left of peak
        low = 0
        high = peak
        while low < high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < target:
                low = mid + 1
            else:
                high = mid
        if mountainArr.get(low) == target:
            return low

        # search in right of peak
        low = peak + 1
        high = length - 1
        while low < high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) > target:
                low = mid + 1
            else:
                high = mid
        if mountainArr.get(low) == target:
            return low
        return -1

if __name__ =="__main__":
    bS = Solution()
    mntArr = MountainArray()
    arr = [1, 2, 5, 10, 8, 7, 9]
    mntArr.arr(arr)
    result=bS.findInMountainArray(7,mntArr)
    print("Element is present at index % d" % result)

