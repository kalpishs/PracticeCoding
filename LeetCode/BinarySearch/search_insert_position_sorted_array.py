"""https://leetcode.com/problems/search-insert-position/"""
from typing import *
class Solution:
    def find(self, nums, start, end, key):
        mid = (start + end) // 2
        if start > end:
            return start
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            return self.find(nums, mid + 1, end, key)
        elif nums[mid] > key:
            return self.find(nums, start, mid - 1, key)

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.find(nums, 0, n-1, target)


if __name__ == "__main__":
    solve = Solution()
    print(solve.searchInsert([1,3,5,6],7))
