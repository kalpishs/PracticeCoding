# Python program to find a peak element in the given array
# Using Binary Search
"""
https://www.geeksforgeeks.org/problems/peak-element/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign
Article:- https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
"""
class Solution:
    def peakElement(self, arr):
        n = len(arr)
        if n < 2:
            return 0
        if arr[0] > arr[1]:
            return 0
        elif arr[n - 1] > arr[n - 2]:
            return n - 1
        low, high = 1, n - 2
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == "__main__":
    arr = [1, 2, 5, 3, 4, 3, 4, 3]
    print(Solution().peakElement(arr))